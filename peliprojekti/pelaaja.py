# Pelaaja

class Pelaaja:


    # Alustetaan pelaaja ja annetaan tarvittavat tiedot

    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.esineet = []
        self.huoneessa = None

    def Liiku(self, huone):
        print("Liiku funktio kutsuttu")
        self.huoneessa = huone


    def KeraaEsine(self, esine):
        self.esineet.append(esine)
        print("Esine ", esine.nimi, "on kerätty")

    def NaytaHuone(self):
        print("Pelaaja on huoneessa_ ", self.huoneessa.nimi)

    def NaytaEsineet(self):
        for esine in self.esineet:
            print("Esine: ", esine.nimi, "Paino: ", esine.paino)