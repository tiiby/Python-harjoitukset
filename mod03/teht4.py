ekaluku_str = input("Anna ensimmäinen kokonaisluku: ")
tokaluku_str = input("Anna toinen kokonaisluku: ")
kolmasluku_str = input ("Anna kolmas kokonaisluku: ")

ekaluku = int(ekaluku_str)
tokaluku = int(tokaluku_str)
kolmasluku = int(kolmasluku_str)

tulo = ekaluku * tokaluku * kolmasluku
summa = ekaluku + tokaluku + kolmasluku
keskiarvo = (ekaluku + tokaluku + kolmasluku) / 3

print("Lukujen tulo: " + str(tulo))
print("Lukujen summa: " + str(summa))
print("Lukujen keskiarvo: " + str(keskiarvo))