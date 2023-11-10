class Ticket(object):
    def __init__(self, name, kategorie, preis):
        self.name = name
        self.kategorie = kategorie
        self.preis = preis

    def __str__(self):
        return "Name: " + self.name + " Kategorie: " + self.kategorie + " Preis: " + str(self.preis)

    def __repr__(self):
        return "Name: " + self.name + " Kategorie: " + self.kategorie + " Preis: " + str(self.preis)

    def __eq__(self, other):
        return self.name == other.name and self.kategorie == other.kategorie and self.preis == other.preis

    def __hash__(self):
        return hash((self.name, self.kategorie, self.preis))

    def getName(self):
        return self.name

    def getKategorie(self):
        return self.kategorie

    def getPreis(self):
        return self.preis

    def setName(self, name):
        self.name = name

    def setKategorie(self, kategorie):
        self.kategorie = kategorie

    def setPreis(self, preis):
        self.preis = preis

    def toDict(self):
        return {'name': self.name, 'kategorie': self.kategorie, 'preis': self.preis}

    def fromDict(self, dict):
        self.name = dict['name']