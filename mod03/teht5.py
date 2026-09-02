leiviskät_str = float(input("Anna leiviskät: "))
naulat_str = float(input("Anna naulat: "))
luodit_str = float(input("Anna luodit: "))

luodit = luodit_str * 13.3
naulat = naulat_str * 425.6
leiviskät = leiviskät_str * 8512

yhteensä_grammoina = leiviskät + naulat + luodit


kilogrammat = int(yhteensä_grammoina // 1000)
grammat = float(yhteensä_grammoina % 1000)


print("Massa nykymittojen mukaan: " + str(kilogrammat) + "kilogrammaa ja " + str(grammat) + " grammaa.")