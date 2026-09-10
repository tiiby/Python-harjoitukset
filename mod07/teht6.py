# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math

def pizza(halkaisija, hinta):
    pizzanhalkaisija = halkaisija / 2
    pizzanpinta_ala_cm2 = math.pi * pizzanhalkaisija**2
    pizzanpinta_ala_m2 = pizzanpinta_ala_cm2 / 1000
    pizzanhinta_per_neliometri = hinta / pizzanpinta_ala_m2
    return pizzanhinta_per_neliometri

eka_pizza_halk = float(input("Anna ensimmäisen pizzan halkaisija: "))
eka_pizza_hint = float(input("Anna ensimmäisen pizzan hinta:"))
toka_pizza_halk = float(input("Anna toisen pizzan halkaisija: "))
toka_pizza_hint = float(input("Anna toisen pizzan hinta: "))

eka_pizza = pizza(eka_pizza_halk, eka_pizza_hint)
toka_pizza = pizza(toka_pizza_halk, toka_pizza_hint)

if eka_pizza < toka_pizza:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
else:
    print("Toinen pizza antaa paremman vastineen rahalle.")
