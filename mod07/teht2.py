# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random


def silmaluku(tahkot):
    nopanheitto = random.randint(1,tahkot)
    return nopanheitto

tahkot = int(input("Anna nopan tahkojen lukumäärä: "))

heitto = silmaluku(tahkot)

print(heitto)

while heitto != tahkot:
    heitto = silmaluku(tahkot)
    print(heitto)