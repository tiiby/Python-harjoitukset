class Huone:
    # Alustetaan huoneet ja huoneen esine
    def __init__(self, nimi, huoneen_esine):
        self.nimi = nimi
        self.huoneen_esine = huoneen_esine
        huoneen_esine = []
        for esine in huoneen_esine:
            huoneen_esine.append(esine)
