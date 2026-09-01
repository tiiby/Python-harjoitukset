pelaajannimi = input("Kerro nimesi: ")
pelaajanikä = int(input("Kerro ikäsi: "))

while pelaajanikä >= 12:

    # Alaikäisen pelaajan peli loppuu
    if pelaajanikä < 12:
        print("Olet liian nuori pelaamaan")
        break


    # Muiden peli jatkuu
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


#Pelin loppu
else:
    print("Loppu")