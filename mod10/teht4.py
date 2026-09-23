# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
# Luokassa on seuraavat metodit:
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä “Suuri romuralli”.
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla,
# onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random

class Kilpailu:

    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in kilpaautot:
            muutos = random.randint(-10,15)
            auto.kiihdyta(muutos)
        for auto in kilpaautot:
            auto.kulje(1)


    def tulosta_tilanne(self):
        print("Rekisteri | Huippunopeus | Nopeus | Matka")
        print("-------------------------------------------")
        for auto in kilpaautot:
            print(f"{auto.rekisteritunnus:9} | {auto.huippunopeus:12} | {auto.nopeus:8} | {auto.matka}")

    def kilpailu_ohi(self):
        for auto in kilpaautot:
            if auto.matka >= 10000:
                voittaja_loytynyt = True

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus < 0:
            uusi_nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            uusi_nopeus = self.huippunopeus
        self.nopeus = uusi_nopeus

    def kulje(self, tunti):
        kuljettu_matka = self.matka + self.nopeus * tunti
        self.matka = kuljettu_matka

kilpaautot = []
jarjestysnumero = 0

for i in range(10):
    tunnus = "ABC-"
    jarjestysnumero += 1
    rekisteritunnus = tunnus + str(jarjestysnumero)
    huippunopeus = random.randint(100, 200)
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    kilpaautot.append(uusi_auto)

voittaja_loytynyt = False

while not voittaja_loytynyt:
    for auto in kilpaautot:
        muutos = random.randint(-10,15)
        auto.kiihdyta(muutos)
    for auto in kilpaautot:
        auto.kulje(1)
    for auto in kilpaautot:
        if auto.matka >= 10000:
            voittaja_loytynyt = True
            break

