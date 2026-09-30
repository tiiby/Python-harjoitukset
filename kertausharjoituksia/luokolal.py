# Tee luokka Kirja. Kirjalla on seuraavat ominaisuudet:
#  nimi
#  kirjoittaja
#  sivumäärä
# Tee luokalle alustaja __init__. Tee lisäksi metodi:
# tulosta_tiedot()
# joka tulostaa kirjan tiedot. Luo ohjelmassa kaksi erilaista Kirja-oliota ja tulosta molempien tiedot metodin avulla.

class Kirja:

    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi} \nKirjailija: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}")


kirja1 = Kirja("Järven neito", "Andrzej Sapkowski", 647)

kirja2 = Kirja("Kapteeni Sinikarhun 13 1/2 elämää", "Walter Moers", 703)

kirja1.tulosta_tiedot()
kirja2.tulosta_tiedot()