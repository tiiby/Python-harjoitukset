pelaajannimi = input("Kerro nimesi: ")
pelaajanikä = int(input("Kerro ikäsi: "))

while pelaajanikä >= 12:
    if pelaajanikä < 12:
        break
    print("Tervetuloa pelaamaan!")
    print("Päävalikko\n1. Laula\n2. Kerro vitsi\n3. Mikä on elämän tarkoitus?")
    komento = input("Anna komento: ")
    if komento == "1.":
        print("Midnigh suuUUuuuUUuuuUUuuuUUUuuun")
        print("Päävalikko\n1. Laula\n2. Kerro vitsi\n3. Mikä on elämän tarkoitus?")
        komento = input("Anna komento: ")
    if komento == "2.":
        print("Sika söi sipsin")
        print("Päävalikko\n1. Laula\n2. Kerro vitsi\n3. Mikä on elämän tarkoitus?")
        komento = input("Anna komento: ")
    if komento == "3.":
        print("42")
        print("Päävalikko\n1. Laula\n2. Kerro vitsi\n3. Mikä on elämän tarkoitus?")
        komento = input("Anna komento: ")
    if komento == "Lopeta":
        break
else:
    print("Loppu")