# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def nestegallona(bensiininmaara):
    litramaara = bensiininmaara * 3.785
    return litramaara

anna_gallonat = float(input("Anna bensiinin määrä gallonina: "))
tulos = nestegallona(anna_gallonat)

while anna_gallonat >= 0:
    print(tulos)
    anna_gallonat = float(input("Anna bensiinin määrä gallonina: "))
else:
    print("Ei negatiivisia lukuja.")