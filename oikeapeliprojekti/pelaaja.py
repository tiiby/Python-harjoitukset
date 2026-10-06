# Pelaaja-olio
class Pelaaja:
    # Alustetaan pelaaja ja annetaan tarvittavat tiedot
    def __init__(self, nimi, ika, aloitushuone, esineet):
        self.nimi = nimi
        self.ika = ika
        self.esineet = esineet
        self.nykyinen_huone = aloitushuone
        self.hp = 15

    # Liikkuu huoneesta toiseen
    def liiku(self, nykyinen_huone):
        self.nykyinen_huone = nykyinen_huone

    # Kerää huoneen esineen
    def keraa_esine(self, esine):
        self.esineet.append(esine)

    def karhuspray(self, kohde):
        kohde.hp -= 14