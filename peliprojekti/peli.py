# Funktiot

def laula():
    nuotti = "\u266B"
    print(nuotti + " Midnigh suuUUuuuUUuuuUUuuuUUUuuun " + nuotti)
    print(päävalikko)

def kerro_vitsi():
    print("Sika söi sipsin")
    print(päävalikko)

def elaman_tarkoitus():
    print("42")
    print(päävalikko)

def lisaa_listalle():
    lisays = input("Anna vitsi tai kirjoita Lopeta: ")
    while lisays != "Lopeta":
        lista.append(lisays)
        lisays = input("Anna seuraava vitsi tai kirjoita Lopeta: ")
    else:
        print(päävalikko)

def tulosta_lista():
    print(lista)

    
# Introtekstitiedosto

with open("peliprojekti/intro.txt", "r") as tiedosto:
    data = tiedosto.read()
    print(data)

# Globaalit muuttujat

pelaajannimi = input("Kerro nimesi: ")
pelaajanika = int(input("Kerro ikäsi: "))
lista = []

print(f"Hei, {pelaajannimi}, {pelaajanika} vuotta.")

# Peli alkaa, kun pelaaja on yli 12-vuotias
while pelaajanika >= 12:
    print(f"Tervetuloa pelaamaan {pelaajannimi}!")
    päävalikko = "Päävalikko\n1. Laula\n2. Kerro vitsi\n3. Mikä on elämän tarkoitus?\n4. Lisää listalle vitsejä\n5. Tulosta lista\n6. Tallenna lista"
    print(päävalikko)

    # Ohjetekstitiedosto

    with open("peliprojekti/ohjeet.txt", "r") as tiedosto:
        data = tiedosto.read()
        print(data)

    # Käyttäjän komennot ja funktiokutsut

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

    if komento == "4.":
        lisaa_listalle()
        komento = input("Anna komento: ")

    if komento == "5.":
        tulosta_lista()
        komento = input("Anna komento: ")

    if komento == "Lopeta":
        break

# Peli loppuu, jos pelaaja on alaikäinen
if pelaajanika < 12:
    print("Olet liian nuori pelaamaan")

# Pelin loppu
else:
    print("Loppu")