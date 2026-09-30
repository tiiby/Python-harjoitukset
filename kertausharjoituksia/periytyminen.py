class Kurssi:
    def __init__(self, nimi):
        self.nimi = nimi

class Opiskelija:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kurssit = []

    def lisaa_kurssi(self, kurssi):
        self.kurssit.append(kurssi.nimi)

opiskelija = Opiskelija("Mikko Mallikas")

kurssi1 = Kurssi("Matematiikka")
kurssi2 = Kurssi("Latina")

opiskelija.lisaa_kurssi(kurssi1)
opiskelija.lisaa_kurssi(kurssi2)

print(opiskelija.nimi, opiskelija.kurssit)