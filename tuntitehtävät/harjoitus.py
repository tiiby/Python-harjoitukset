kayttajan_lampotila = input("Anna lämpötila tai lopeta painamalla Enter: ")

if kayttajan_lampotila != "":
    matalin = int(kayttajan_lampotila)
    korkein = int(kayttajan_lampotila)
    maara = 0
    summa = 0

    while kayttajan_lampotila != "":
        lampo = int(kayttajan_lampotila)
        maara = maara + 1
        summa = summa + lampo

        if lampo >= korkein:
            korkein = lampo
        if lampo <= matalin:
            matalin = lampo
        
        kayttajan_lampotila = input("Anna lämpötila: ")

    keskiarvo = summa / maara


    print(f"Korkein lämpötila: {korkein}\nMatalin lämpötila: {matalin}\nLämpötilojen keskiarvo: {keskiarvo}")