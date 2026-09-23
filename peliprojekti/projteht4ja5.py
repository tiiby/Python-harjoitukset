from pelaaja import Pelaaja
from esine import Esine
from huone import Huone
import json

def tallenna(pelaaja1):

    nimi = pelaaja1.nimi
    ika = pelaaja1.ika
    esineet = []
    for item in pelaaja1.esineet:
        esineet.append({
            "nimi": item.nimi,
            "paino": item.paino
        })
    huoneessa = pelaaja1.huoneessa

    pelaajan_data = {
        "pelaajan_nimi": nimi,
        "pelaajan_ika": ika,
        "esineet": esineet,
        "huoneessa": huoneessa
    }

    with open("peliprojekti/tallennus.txt", "w") as tiedosto:
        json.dump(pelaajan_data, tiedosto)

pelaajannimi = input("Kerro nimesi: ")
pelaajanika = int(input("Kerro ikäsi: "))

pelaaja1 = Pelaaja(pelaajannimi, pelaajanika)


esine = Esine("Lusikka", 2)
esine2 = Esine("Haarukka", 3)
huone = Huone("Olohuone", "sohva")


huone.MitaOnHuoneessa()
pelaaja1.KeraaEsine(esine)
pelaaja1.KeraaEsine(esine2)
pelaaja1.NaytaEsineet()
tallenna(pelaaja1)


with open("peliprojekti/tallennus.txt", "r") as tiedosto:
    data_luettu = json.load(tiedosto)

nimi = data_luettu["pelaajan_nimi"]

if nimi == "":
    pelaajannimi = input("Kerro nimesi: ")
    pelaajanika = int(input("Kerro ikäsi: "))
    pelaaja1 = Pelaaja(pelaajannimi, pelaajanika)


else:
    with open("peliprojekti/tallennus.txt", "r") as tiedosto:
        data_luettu = json.load(tiedosto)
    print(f"Pelaaja: {data_luettu['pelaajan_nimi']}, ikä: {data_luettu['pelaajan_ika']}, esineet: {data_luettu['esineet']}")


    ika = data_luettu["pelaajan_ika"]
    esineet = []
    for esine in data_luettu["esineet"]:
        uusi_esine = Esine(esine['nimi'], esine['paino'])
        esineet.append(uusi_esine)

    huoneessa = data_luettu["huoneessa"]
    uusi_pelaaja = Pelaaja(nimi, ika)
    uusi_pelaaja.esineet = esineet
    uusi_pelaaja.huoneessa = huoneessa
