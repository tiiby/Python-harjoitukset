# Nyt ohjelmoidaan autokilpailu.
# Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti “ABC-1”, “ABC-2” jne.
# Sitten kilpailu alkaa.
# 
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

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

print("Rekisteri | Huippunopeus | Matka")
print("-------------------------------------------")
for auto in kilpaautot:
    print(f"{auto.rekisteritunnus:9} | {auto.huippunopeus:12} | {auto.matka}")

