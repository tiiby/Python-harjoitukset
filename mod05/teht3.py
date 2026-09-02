# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

käyttäjän_luku = input("Anna luku tai lopeta painamalla Enter: ")

while käyttäjän_luku != "":
    print(käyttäjän_luku)
    käyttäjän_luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")
if käyttäjän_luku == "":
