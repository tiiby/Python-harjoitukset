luku = int(input("Anna kokonaisluku: "))
maara = 0

while luku != 999:
    if luku % 4 == 0:
        maara += 1
    luku = int(input("Anna kokonaisluku: "))
print(maara)