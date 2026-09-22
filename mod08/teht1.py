# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if kuukausi == 12:
    indeksi = 0
else:
    indeksi = (kuukausi - 1) // 3

print(f"Vuodenaika on {vuodenajat[indeksi]}.")