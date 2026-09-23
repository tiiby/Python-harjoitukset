# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Talo:

    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lukumaara = hissien_lukumaara
        hissit = []
        for hissi in range(hissien_lukumaara):
            hissit.append = hissi

    def aja_hissia(self, hissinumero, kohdekerros):
        self.hissinumero = hissinumero
        self.kohdekerros = kohdekerros

class Hissi:
    
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin


    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}.")

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self, siirry):
        while self.nykyinen_kerros < siirry:
            self.kerros_ylos()
        while self.nykyinen_kerros > siirry:
            self.kerros_alas()