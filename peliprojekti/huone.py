# Huone

class Huone:

    # Alustetaan huone ja huoneen esineet

    def __init__(self, nimi, esine):
        self.nimi = nimi
        self.esine = esine

    def MitaOnHuoneessa(self):
        print(self.nimi, ":ssa on tämä esine:", self.esine)