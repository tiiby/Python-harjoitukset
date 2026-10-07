from pelaaja import Pelaaja
from huoneet import Huone
from karhu import Karhu
import json
import os

# Tallennusfunktio
def tallenna(pelaaja):

    nimi = pelaaja.nimi
    ika = pelaaja.ika
    esineet = []
    huone = pelaaja.nykyinen_huone.nimi
    for item in pelaaja.esineet:
        esineet.append(item)

    pelaajan_data = {
        "pelaajan_nimi": nimi,
        "pelaajan_ika": ika,
        "esineet": esineet,
        "huone": huone
    }

    with open("oikeapeliprojekti/save.json", "w") as tiedosto:
        json.dump(pelaajan_data, tiedosto)

    print("Pelaaja tallennettu")

# Aiemman tallennuksen haku
def tallennuksen_haku(huoneet):

    try:
        with open("oikeapeliprojekti/save.json", "r") as tiedosto:
            pelaajan_data = json.load(tiedosto)
            pelaajannimi = pelaajan_data["pelaajan_nimi"]
            pelaajanika = pelaajan_data["pelaajan_ika"]
            pelaajan_esineet = pelaajan_data["esineet"]
            huoneen_nimi = pelaajan_data["huone"]
            nykyinen_huone = huoneet[huoneen_nimi]
            
            pelaaja = Pelaaja(pelaajannimi, pelaajanika, nykyinen_huone, pelaajan_esineet)
            print("\nTallennus löydetty!\n")

            return pelaaja
    except:
        return None

# Ohjeteksti
def ohjeet():
    with open("oikeapeliprojekti/ohjeet.txt", "r") as tiedosto:
        data = tiedosto.read()
        print(data)

# Introteksti
def intro():
    with open("oikeapeliprojekti/intro.txt", "r") as tiedosto:
        data = tiedosto.read()
        print(data)


# Antaa tiedon missä huoneessa ollaan ja mitä huoneessa on
def status():
    print("*****************")
    print(f"Olet tällä hetkellä {pelaaja.nykyinen_huone.nimi}\nSinulla on {pelaaja.esineet}")
    if len(pelaaja.nykyinen_huone.huoneen_esine) > 0:
        print(f"Näet {pelaaja.nykyinen_huone.huoneen_esine}")
    print("*****************")


# Globaalit muuttujat
pelaajannimi = input("Kerro nimesi: ")
pelaajanika = int(input("Kerro ikäsi: "))

# Peli alkaa, kun pelaaja on yli 12-vuotias
if pelaajanika >= 12:
    
    # Luodaan huoneet, pelaaja ja karhu
    karhu = Karhu("karhu")
    metsan_reuna = Huone("metsänreunassa", "karhuspray")
    metsa = Huone("metsässä", "roskia")
    syvempi_metsa = Huone("syvemmällä metsässä", karhu)

    huoneet = {
        "metsänreunassa": metsan_reuna,
        "metsässä": metsa,
        "syvemmällä metsässä": syvempi_metsa
    }

    # Tarkistetaan onko nimellä tallennusta
    if os.path.exists("oikeapeliprojekti/save.json"):
        pelaaja = tallennuksen_haku(huoneet)
        if pelaaja == None:
            pelaaja = Pelaaja(pelaajannimi, pelaajanika, metsan_reuna, ["roskapussi"])
        if pelaaja.nimi != pelaajannimi or pelaaja.ika != pelaajanika:
            pelaaja = Pelaaja(pelaajannimi, pelaajanika, metsan_reuna, ["roskapussi"])
    # Jos ei ole, niin tehdään uusi pelaaja
    else:
        pelaaja = Pelaaja(pelaajannimi, pelaajanika, metsan_reuna, ["roskapussi"])

    # Introtekstitiedosto
    intro()

    # Ohjetekstitiedosto
    ohjeet()

    # Pelin looppi
    while True:

        status()

        toimi = input("Mitä teet? ").lower().split(" ", 1)

        # Virheellisten inputtien käsittelyä
        komennot = ["kerää", "liiku", "tallenna"]

        if toimi[0] not in komennot:
            print("Anna toimiva komento.")
            continue
        if toimi[0] == "kerää" and len(toimi) == 1:
            print("Komennon muoto: kerää <esine>")
            continue
        if toimi[0] == "liiku" and len(toimi) == 1:
            print("Komennon muoto: liiku <suunta>")
            continue
        if toimi[0] == "tallenna" and len(toimi) != 1:
            print("Komennon muoto: tallenna")
            continue

        # Tavaroiden kerääminen ja poistaminen huoneista
        if toimi[0] == "kerää" and len(toimi) == 2:
            if len(pelaaja.nykyinen_huone.huoneen_esine) == 0:
                print("Huone on tyhjä.")
            elif toimi[1] in pelaaja.nykyinen_huone.huoneen_esine:
                pelaaja.keraa_esine(toimi[1])
                pelaaja.nykyinen_huone.poista_esine(toimi[1])
            else:
                print("Tätä esinettä ei ole huoneessa.")

        # Liikkuminen huoneiden välillä
        if toimi[0] == "liiku" and len(toimi) == 2:
            if toimi[1] in huoneet:
                pelaaja.liiku(huoneet[toimi[1]])
            else:
                print("Et voi liikkua tänne.")
            
        # Peli tilanteen tallentaminen
        if toimi[0] == "tallenna" and len(toimi) == 1:
            tallenna(pelaaja)
            break

        # Pelin voittaminen
        if "roskapussi" in pelaaja.esineet and "roskia" in pelaaja.esineet and pelaaja.nykyinen_huone == metsan_reuna:
            print("Olet kerännyt roskat metsästä ja metsä on puhdas taas!\nMetsän eläimet kiittävät sinua ja voit viedä roskat roskiin.")
            break

        # Pelin häviäminen kahdella tapaa
        if pelaaja.nykyinen_huone == syvempi_metsa:
            if "karhuspray" in pelaaja.esineet:
                pelaaja.karhuspray(karhu)
                print("Oi ei! Syvemmällä metsässä vastaan tuli karhu, mutta onneksi sinulla on karhuspray mukana.\nSait karhun karkotettua ja juostua pakoon, mutta koska metsä on edelleen täynnä roskia, hävisit pelin.")
                quit()
            else:
                karhu.purema(pelaaja)
                print("Oi ei! Syvemmällä metsässä vastaan tuli karhu ja jouduit karhun ruuaksi elämän kiertokulkuun")
                quit()

# Peli loppuu, jos pelaaja on alaikäinen
if pelaajanika < 12:
    print("Olet liian nuori pelaamaan")

# Pelin loppu
else:
    print("Loppu")