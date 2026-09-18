# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class Auto:
    nopeus = 0
    matka = 0

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

    def kiihdyta(self, muutos):
        self.muutos = muutos
        nopeus = 0
        nopeuden_muutos = nopeus + muutos
        return nopeuden_muutos



auto1 = Auto("ABC_123", 142)

print(f"Ensimmäisen auton rekisterinumero on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus}km/h.")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton nopeus nyt: {auto1.muutos}km/h")

auto1.kiihdyta(-200)

print(f"Auton nopeus nyt: {auto1.muutos}km/h")