# Huoneen alustus
class Huone:
    # Alustetaan huoneet ja huoneen esine
    def __init__(self, nimi, huoneen_esine):
        self.nimi = nimi
        self.huoneen_esine = []
        self.huoneen_esine.append(huoneen_esine)

    def poista_esine(self, esine):
        self.huoneen_esine.remove(esine)