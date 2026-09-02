# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#  Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
#  Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#  Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
#  (Oikea käyttäjätunnus on python ja salasana rules).

käyttäjätunnus = "python"
salasana = "rules"

annettu_käyttäjätunnus = input("Anna käyttäjätunnus: ")
annettu_salasana = input("Anna salasana: ")
kysytyt_kerrat = 1

while (annettu_käyttäjätunnus != käyttäjätunnus or annettu_salasana != salasana) and kysytyt_kerrat < 5:
    annettu_käyttäjätunnus = input("Anna käyttäjätunnus: ")
    annettu_salasana = input("Anna salasana: ")
    kysytyt_kerrat = kysytyt_kerrat + 1
if annettu_käyttäjätunnus == käyttäjätunnus and annettu_salasana == salasana:
        print("Tervetuloa")
else:
    print("Pääsy evätty")