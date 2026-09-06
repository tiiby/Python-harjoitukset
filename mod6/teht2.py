# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

def tervehdi(kerrat):
    for i in range(kerrat):
        print("Hyvää päivää " + str(i+1) + ". kerran")
    return

print("Päivä alkaa tervehdyksillä.")
tervehdi(5)
print("Tervehditään lisää.")
tervehdi(2)