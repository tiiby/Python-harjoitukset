# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def nestegallona(gallona):
    litramaara = gallona * 3.785
    return litramaara

anna_gallona = float(input("Anna bensiinin määrä nestegallonoina: "))

while anna_gallona >= 0:
    tulos = nestegallona(anna_gallona)
    print(f"{anna_gallona} gallonaa on litroina {tulos:.2f}.")
    anna_gallona = float(input("Anna bensiinin määrä nestegallonoina: "))