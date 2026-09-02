# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, 
# kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

tietokoneen_luku = random.randint(0,10)

arvattu_luku = int(input("Arvaa minkä luvun valitsin väliltä 1-10? "))

while arvattu_luku != tietokoneen_luku:
    if arvattu_luku < tietokoneen_luku:
        print("Liian pieni arvaus")
        arvattu_luku = int(input("Anna toinen luku: "))
    if arvattu_luku > tietokoneen_luku:
        print("Liian suuri arvaus")
        arvattu_luku = int(input("Anna toinen luku: "))
print("Oikein!")
