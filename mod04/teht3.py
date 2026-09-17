# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.


sukupuoli = input("Oletko biologisesti mies vai nainen (n/m)? ")
nainen = "n"
mies = "m"

if sukupuoli == "n":
    hemoglob = float(input("Mikä on hemoglobiiniarvosi? "))
    if hemoglob > 175:
        print("Hemoglobiinisi on korkea.")
    elif 117 <= hemoglob < 175:
        print("Hemoglobiinisi on normaali.")
    elif hemoglob <117:
        print("Hemoglobiinisi on matala.")


elif sukupuoli == "m":
    hemoglob = float(input("Mikä on hemoglobiiniarvosi? "))
    if hemoglob > 195:
        print("Hemoglobiinisi on korkea.")
    elif 134 <= hemoglob < 195:
        print("Hemoglobiinisi on normaali.")
    elif hemoglob <134:
        print("Hemoglobiinisi on matala.")
else:
    print("Anna biologinen sukupuoli.")