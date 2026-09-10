kayttajan_ika = int(input("Minkä ikäinen olet: "))

if kayttajan_ika >= 18:
    print("Olet täysi-ikäinen.")
else:
    print("Olet alaikäinen.")


kayttajan_nimi = input("Anna nimesi: ")

for i in kayttajan_nimi:
    print(i)



kayttajan_luku = input("Anna luku tai lopeta painamalla Enter: ")

maara = 0
summa = 0

while kayttajan_luku != "":
    luku = int(kayttajan_luku)
    maara = maara + 1
    summa = summa + luku

    kayttajan_luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")

print("Lukuja annettiin:", maara)
print("Lukujen summa:", summa)