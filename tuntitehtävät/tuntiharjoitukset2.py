eka_merkkijono = input("Anna merkkijono: ")
toka_merkkijono = input("Anna toinen merkkijono: ")

eka_pituus = len(eka_merkkijono)
toka_pituus = len(toka_merkkijono)

if eka_pituus > toka_pituus:
    print("Ensimmäinen on pidempi")
elif toka_pituus > eka_pituus:
    print("Toinen on pidempi")
else:
    print("Yhtä pitkiä")

luku = int(input("Anna kokonaisluku: "))
maara = 0

while luku != 999:
    if luku % 4 == 0:
        maara += 1
print(maara)

lista = [-3, 12, -1, 7, -9, 4, 0, 15]

uusi_lista = []

for i in lista:
    if i >= 0:
        uusi_lista.append(i)

print(uusi_lista)