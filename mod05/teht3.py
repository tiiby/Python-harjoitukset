# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

käyttäjän_luku = input("Anna luku tai lopeta painamalla Enter: ")

if käyttäjän_luku != "":
    pienin = int(käyttäjän_luku)
    suurin = int(käyttäjän_luku)

    while käyttäjän_luku != "":
        uusi_luku = int(käyttäjän_luku)

        if uusi_luku < pienin:
            pienin = uusi_luku
        if uusi_luku > suurin:
            suurin = uusi_luku

        käyttäjän_luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")

    print(f"Suurin luku: {suurin}\nPienin luku: {pienin}")
