leiviskät_str = input("Anna leiviskät: ")
naulat_str = input("Anna naulat: ")
luodit_str = input("Anna luodit: ")

leiviskät = float(leiviskät_str)
naulat = float(naulat_str)
luodit = float(luodit_str)

yhteensä_grammaa = (leiviskät * 8512) + (naulat * 425,6) + (luodit * 13,3)

kilogrammat = int(yhteensä_grammaa // 1000)
grammat = float(yhteensä_grammaa % 1000)

print("Massa nykymittojen mukaan: " + str(kilogrammat) + "kilogrammaa ja " + str(grammat) + " grammaa.")