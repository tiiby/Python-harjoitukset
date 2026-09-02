# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma = float(input("Anna tuumamäärä: "))

while tuuma >= 0:
    tuumaa_senteiksi = tuuma * 2.54
    print(f"{tuuma} tuumaa on {tuumaa_senteiksi} senttimetriä")
    tuuma = float(input("Anna tuumamäärä: "))
else:
    print(str("Et voi syöttää negatiivisia lukuja."))