# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

    def kulje(self, aika):
        


auto1 = Auto("ABC_123", 142)

print(f"Ensimmäisen auton rekisterinumero on {auto1.rekisteritunnus} ja huippunopeus on {auto1.huippunopeus}km/h.")

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton nopeus nyt: {auto1.muutos}km/h")

auto1.kiihdyta(-200)

print(f"Auton nopeus nyt: {auto1.muutos}km/h")