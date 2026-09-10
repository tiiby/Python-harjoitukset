# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random


def silmaluku():
    nopanheitto = random.randint(1,6)
    return nopanheitto

heitto = silmaluku()

print(heitto)

while heitto != 6:
    heitto = silmaluku()
    print(heitto)
