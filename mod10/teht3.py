# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Talo:


    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lukumaara = hissien_lukumaara
        self.hissit = []
        for hissi in range(hissien_lukumaara):
            hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissia(self, hissinumero, kohdekerros):
        hissi = self.hissit[hissinumero -1]
        self.kohdekerros = kohdekerros
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


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

talo = Talo(1, 25, 2)

talo.aja_hissia(1, 6)
talo.aja_hissia(1, 3)
talo.aja_hissia(1, 25)

talo.aja_hissia(2, 3)
talo.aja_hissia(2, 1)

talo.palohalytys()