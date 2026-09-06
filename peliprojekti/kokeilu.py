def laula():
    nuotti = "\u266B"
    print(nuotti + " Midnigh suuUUuuuUUuuuUUuuuUUUuuun " + nuotti)
    print(päävalikko)
    return

def kerro_vitsi():
    print("Sika söi sipsin")
    print(päävalikko)
    return

def elaman_tarkoitus():
    print("42")
    print(päävalikko)
    return




pelaajannimi = input("Kerro nimesi: ")
pelaajanikä = int(input("Kerro ikäsi: "))

print(f"Hei, {pelaajannimi}, {pelaajanikä} vuotta.")

# Peli alkaa, kun pelaaja on yli 12-vuotias
while pelaajanikä >= 12:
    print(f"Tervetuloa pelaamaan {pelaajannimi}!")
    päävalikko = "Päävalikko\n1. Laula\n2. Kerro vitsi\n3. Mikä on elämän tarkoitus?\nLopettaaksesi, kirjoita 'Lopeta'"
    print(päävalikko)
    komento = input("Anna komento: ")
    if komento == "1.":
        laula()
        komento = input("Anna komento: ")
    if komento == "2.":
        kerro_vitsi()
        komento = input("Anna komento: ")
    if komento == "3.":
        elaman_tarkoitus()
        komento = input("Anna komento: ")
    if komento == "Lopeta":
        break

# Peli loppuu, jos pelaaja on alaikäinen
if pelaajanikä < 12:
    print("Olet liian nuori pelaamaan")

# Pelin loppu
else:
    print("Loppu")