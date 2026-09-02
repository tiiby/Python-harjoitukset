pelaajannimi = input("Kerro nimesi: ")
pelaajanikä = int(input("Kerro ikäsi: "))

print(f"Hei, {pelaajannimi}, {pelaajanikä} vuotta.")

# Peli alkaa, kun pelaaja on yli 12-vuotias
while pelaajanikä >= 12:
    print(f"Tervetuloa pelaamaan {pelaajannimi}!")
    päävalikko = "Päävalikko\n1. Laula\n2. Kerro vitsi\n3. Mikä on elämän tarkoitus?"
    print(päävalikko)
    komento = input("Anna komento: ")
    if komento == "1.":
        nuotti = "\u266B"
        print(nuotti + " Midnigh suuUUuuuUUuuuUUuuuUUUuuun " + nuotti)
        print(päävalikko)
        komento = input("Anna komento: ")
    if komento == "2.":
        print("Sika söi sipsin")
        print(päävalikko)
        komento = input("Anna komento: ")
    if komento == "3.":
        print("42")
        print(päävalikko)
        komento = input("Anna komento: ")
    if komento == "Lopeta":
        break

# Peli loppuu, jos pelaaja on alaikäinen
if pelaajanikä < 12:
    print("Olet liian nuori pelaamaan")

# Pelin loppu
else:
    print("Loppu")