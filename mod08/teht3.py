# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)


lentoasemat = {"EFHK": "Helsinki", "EGLL": "Lontoo", "RJTT": "Tokio", "KORD": "Chicago", "EFOUL": "Oulu", "LFPG": "Pariisi"}

kayttajanteko = input("Haluatko lisätä listaan (Lisää), hakea lentoasemaa listalta (Haku) vai lopettaa (Lopeta)? ")

while kayttajanteko != "Lopeta":
    if kayttajanteko == "Lisää":
        lentasnimi = input("Anna lentoaseman nimi:")
        ICAO = input("Anna ICAO-koodi: ")
        lentoasemat[ICAO] = lentasnimi
    elif kayttajanteko == "Haku":
        haku = input("Anna lentoaseman ICAO-koodi: ")
        if haku in lentoasemat:
            print(lentoasemat[haku])
    kayttajanteko = input("Haluatko lisätä listaan (Lisää), hakea lentoasemaa listalta (Haku) vai lopettaa (Lopeta)? ")