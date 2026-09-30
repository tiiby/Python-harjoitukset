# Tee luokka Elain. Luokassa on metodi:
# aantele()
# Tee Elain-luokasta periytyvät luokat:
# Koira
# Kissa
# Määrittele molemmille oma versio aantele()-metodista.
# Luo eläimet listaan:
# elaimet = [...]
# Käy lista läpi silmukalla ja kutsu jokaisen eläimen aantele()-metodia.

class Elain:

    def aantele():
        print("???")

class Koira(Elain):

    def aantele():
        print("Hau hau hau")

class Kissa(Elain):

    def aantele():
        print("")