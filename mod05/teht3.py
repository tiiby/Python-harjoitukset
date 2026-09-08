# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

käyttäjän_luku = input("Anna luku tai lopeta painamalla Enter: ")

while käyttäjän_luku != "":
    käyttäjän_luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")
else:
    pienin_luku = min(käyttäjän_luku)
    suurin_luku = max(käyttäjän_luku)
    print("Pienin luku: " + pienin_luku + " ja suurin luku: " + suurin_luku)