class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Construtor chamado")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Au Au!")

    def __del__(self):
        print("Removendo o objeto da memória")

c = Cachorro("Rex", "Marrom")
print(c.nome)
print(c.latir())

