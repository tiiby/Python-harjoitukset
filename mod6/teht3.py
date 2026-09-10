# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.


kokonaisluku = int(input("Anna kokonaisluku: "))

if kokonaisluku == 0 or kokonaisluku == 1:
    print(f"{kokonaisluku} ei ole alkuluku.")

jakaja_loytyi = 0

for alkuluku in range(2, kokonaisluku):
    if kokonaisluku % alkuluku == 0:
        jakaja_loytyi = 1
        break

        
if jakaja_loytyi == 0:
    print(f"{kokonaisluku} on alkuluku.")
if jakaja_loytyi == 1:
    print(f"{kokonaisluku} ei ole alkuluku.")