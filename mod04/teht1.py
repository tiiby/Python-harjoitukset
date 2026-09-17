# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.


kuhanpituus = float(input("Anna kuhan pituus senttimetreinä: "))

if kuhanpituus < 37:
    alamitta = 37 - kuhanpituus
    print("Kuha on " + str(alamitta) + " senttiä alamittainen. Päästä kala veteen.")