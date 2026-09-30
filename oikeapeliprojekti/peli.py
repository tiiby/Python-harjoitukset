from pelaaja import Pelaaja
from huoneet import Huone
import json

# Funktiot

# Tallennusfunktio
def tallenna(pelaaja):

    nimi = pelaaja.nimi
    ika = pelaaja.ika
    esineet = []
    for item in pelaaja.esineet:
        esineet.append({
            "nimi": item,
        })

    pelaajan_data = {
        "pelaajan_nimi": nimi,
        "pelaajan_ika": ika,
        "esineet": esineet,
    }

    with open("oikeapeliprojekti/save.json", "w") as tiedosto:
        json.dump(pelaajan_data, tiedosto)

    print("Pelaaja tallennettu")

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

# Kerää huoneen esineen pelaajalle
def keraa_esine(esine):
    pelaaja.esineet.append(esine)

# Antaa tiedon missä huoneessa ollaan ja mitä huoneessa on
def status():
    print("*****************")
    print(f"Olet tällä hetkellä {nykyinen_sijainti.nimi}\nSinulla on {pelaaja.esineet}")
    print(f"Näet {nykyinen_sijainti.huoneen_esine}")
    print("*****************")


# Globaalit muuttujat
pelaajannimi = input("Kerro nimesi: ")
pelaajanika = int(input("Kerro ikäsi: "))

# Peli alkaa, kun pelaaja on yli 12-vuotias
if pelaajanika >= 12:
    
    # Tähän olemassa olevan tallennuksen tarkastaminen?

    pelaaja = Pelaaja(pelaajannimi, pelaajanika)

    # Introtekstitiedosto
    intro()

    # Ohjetekstitiedosto
    ohjeet()

    metsan_reuna = Huone("Metsänreunassa", "karhuspray")
    metsa = Huone("Metsässä", "roskia")
    syvempi_metsa = Huone("Syvemmällä metsässä", "Karhu")

    nykyinen_sijainti = metsan_reuna

    # Pelin looppi
    
    while True:

        status()

        toimi = input("Mitä teet? ").lower()


        toimi = toimi.split(" ", 1)

        # Tavaroiden kerääminen ja poistaminen huoneista
        if toimi[0] == "kerää":
            if toimi[1] in nykyinen_sijainti.huoneen_esine:
                keraa_esine(toimi[1])
                print(f"Sinulla on nyt {pelaaja.esineet}")
            else:
                print(f"Ei täällä ole mitään!")

        # Liikkuminen huoneiden välillä
        if toimi[0] == "liiku":
            if toimi[1] != nykyinen_sijainti:
                nykyinen_sijainti = toimi[1]
                print(f"Olet nyt {nykyinen_sijainti}")

        # Peli tilanteen tallentaminen
        if toimi[0] == "tallenna":
            tallenna(pelaaja)
            break

        # Pelin voittaminen
        if "roskapussi" in pelaaja.esineet and "roskia" in pelaaja.esineet:
            print("Olet kerännyt roskat metsästä ja metsä on puhdas taas!\nMetsän eläimet kiittävät sinua ja voit viedä roskat roskiin.")

        # Pelin häviäminen kahdella tapaa
        if nykyinen_sijainti == syvempi_metsa:
            if "karhuspary" in pelaaja.esineet:
                print("Oi ei! Syvemmällä metsässä vastaan tuli karhu, mutta onneksi sinulla on karhuspray mukana.\nSait karhun karkotettua ja juostua pakoon.")
                break
            else:
                print("Oi ei! Syvemmällä metsässä vastaan tuli karhu ja jouduit karhun ruuaksi elämän kiertokulkuun")
                break


# Peli loppuu, jos pelaaja on alaikäinen
if pelaajanika < 12:
    print("Olet liian nuori pelaamaan")

# Pelin loppu
else:
    print("Loppu")