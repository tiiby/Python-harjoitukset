leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luoti_grammoina = luodit * 13,3
naula_grammoina = naulat * 32 * 13,3
leiviskät_grammoina = leiviskät * 20 * 32 * 13,3

yhteisgrammat = luoti_grammoina + naula_grammoina + leiviskät_grammoina

kilogrammat = int(yhteisgrammat // 1000)
grammat = float(yhteisgrammat % 1000)

print("Massa nykymittojen mukaan: " + str(kilogrammat) + "kilogrammaa ja " + str(grammat) + " grammaa.")