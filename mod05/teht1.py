# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

eka = 1

while eka <= 1000:
    if eka % 3 == 0:
        print(eka)
    eka = eka + 1