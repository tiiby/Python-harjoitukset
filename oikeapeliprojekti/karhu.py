class Karhu:

    def __init__(self, nimi):
        self.nimi = nimi
        self.hp = 15

    def purema(self, kohde):
        kohde.hp -= 15