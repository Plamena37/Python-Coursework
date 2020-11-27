class Taxes:
    def __init__(self):
        self.by_names = {}


    def add_taxes(self, name, tok, voda, telefon):
        self.tok = tok
        self.voda = voda
        self.telefon = telefon
        self.name = name
        self.by_names[self.name] = {"Tok": self.tok, "Voda": self.voda, "Telefon": self.telefon}



