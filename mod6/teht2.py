# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

numerot = []

anna_numero = input("Anna numero tai lopeta painamalla Enter: ")

while anna_numero != "":
    numeroint = int(anna_numero)
    numerot.append(numeroint)
    anna_numero = input("Anna numero: ")
    
numerot.sort(reverse = True)
print(numerot[0:5])
