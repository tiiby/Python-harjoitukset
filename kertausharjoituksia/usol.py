# Tee luokka Opiskelija. Opiskelijalla on nimi ja pistemäärä.
# Luo vähintään kolme opiskelijaoliota ja tallenna ne listaan. Käy lista läpi silmukan avulla ja tulosta jokaisen
# opiskelijan nimi ja pistemäärä.
# Lisätehtävä
# Tulosta vain ne opiskelijat, joiden pistemäärä on vähintään 50

class Opiskelija:

    def __init__(self, nimi, pistemaara):
        self.nimi = nimi
        self.pistemaara = pistemaara

opiskelijat = []

opiskelija1 = Opiskelija("Matti Myöhänen", 180)
opiskelija2 = Opiskelija("Hilkka Hikari", 14)
opiskelija3 = Opiskelija("Milla Mallioppilas", 200)

opiskelijat.append(opiskelija1)
opiskelijat.append(opiskelija2)
opiskelijat.append(opiskelija3)

for opiskelija in opiskelijat:
    if opiskelija.pistemaara > 50:
        print(opiskelija.nimi, opiskelija.pistemaara)