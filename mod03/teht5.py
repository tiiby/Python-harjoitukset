leiviskät_str = input("Anna leiviskät: ")
naulat_str = input("Anna naulat: ")
luodit_str = input("Anna luodit: ")

luodit = luodit_str * 13,3
naulat = naulat_str * 425,6
leiviskät = leiviskät_str * 8512

yhteensä_grammoina = float(leiviskät + naulat + luodit)

kilogrammat = int(yhteensä_grammoina // 1000)
grammat = float(yhteensä_grammoina % 1000)

print(f"Massa nykymittojen mukaan: " + {kilogrammat} + "kilogrammaa ja " + {grammat:.1f} + " grammaa.")