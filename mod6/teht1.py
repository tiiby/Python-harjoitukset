# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random

noppienluvut = []

montako_noppaa = int(input("Kuinka monta kertaa heitetään noppaa: "))

for silmaluku in range(montako_noppaa):
    silmaluku = random.randint(1,6)
    noppienluvut.append(silmaluku)
    

summa = sum(noppienluvut)
print(summa)