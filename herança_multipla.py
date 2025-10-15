class mamifero:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som de mamífero"
    
class ave(mamifero):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.cor = cor

    def voar(self):
        return f"{self.nome} está voando."

    def emitir_som(self):
        return "Som de ave"
    
class morcego(mamifero, ave):
    def __init__(self, nome, cor, envergadura):
        mamifero.__init__(self, nome)
        ave.__init__(self, nome, cor)
        self.envergadura = envergadura

    def emitir_som(self):
        return "Som de morcego"