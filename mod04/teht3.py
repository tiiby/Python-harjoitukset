sukupuoli = input("Oletko biologisesti mies vai nainen (n/m)? ")
nainen = "n"
mies = "m"

if sukupuoli == "n":
    hemoglob = float(input("Mikä on hemoglobiiniarvosi? "))
    if hemoglob > 175:
        print("Hemoglobiinisi on korkea.")
    if 117 <= hemoglob < 175:
        print("Hemoglobiinisi on normaali.")
    if hemoglob <117:
        print("Hemoglobiinisi on matala.")


if sukupuoli == "m":
    hemoglob = float(input("Mikä on hemoglobiiniarvosi? "))
    if hemoglob > 195:
        print("Hemoglobiinisi on korkea.")
    if 134 <= hemoglob < 195:
        print("Hemoglobiinisi on normaali.")
    if hemoglob <134:
        print("Hemoglobiinisi on matala.")