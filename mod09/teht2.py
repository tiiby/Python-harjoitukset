# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

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


auto1 = Auto("ABC_123", 142)

print(f"Auton rekisterinumero on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus}km/h. Auton tämänhetkinen nopeus on {auto1.nopeus} km/h ja kuljettu matka on {auto1.matka}")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)


print(f"Auton nopeus nyt: {auto1.nopeus} km/h")

auto1.kiihdyta(-200)

print(f"Auton nopeus nyt: {auto1.nopeus} km/h")