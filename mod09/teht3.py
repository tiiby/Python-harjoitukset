# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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



auto1 = Auto("ABC_123", 142)

print(f"Auton rekisterinumero on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus}km/h. Auton tämänhetkinen nopeus on {auto1.nopeus} km/h ja kuljettu matka on {auto1.matka}")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

auto1.kulje(2)

print(f"Kuljettu matka on {auto1.matka} km")

print(f"Auton nopeus nyt: {auto1.nopeus} km/h")

auto1.kiihdyta(-200)

print(f"Auton nopeus nyt: {auto1.nopeus} km/h")