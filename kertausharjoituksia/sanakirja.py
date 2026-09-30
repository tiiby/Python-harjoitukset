# Tee sanakirja, joka kuvaa tuotetta. Tallenna tuotteesta nimi, hinta ja varastosaldo.
# Ohjelmassa pitää tämän jälkeen:
# 1. tulostaa tuotteen tiedot
# 2. muuttaa tuotteen hintaa
# 3. vähentää varastosaldoa yhdellä
# 4. lisätä sanakirjaan uusi tieto tuoteryhma
# 5. tulostaa lopullinen sanakirja

tuotteet = {

    "Tuote": "Banaani",
    "Hinta": 2.30,
    "Varastosaldo": 5

}

print(tuotteet)

tuotteet["Hinta"] = 0.30
tuotteet["Varastosaldo"] -= 1
tuotteet["Kollimäärä"] = 2

print(tuotteet)