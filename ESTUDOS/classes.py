class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1  # marcha inicial

    def buzinar(self):
        return "Buzina: Beep Beep!"

    def empinar(self):
        return "A bicicleta está empinando!"
    def trocar_marcha(self, marcha):
        return f"A bicicleta trocou para a marcha {marcha}."
# Exemplo de uso da classe bicicleta
        def _trocar_marcha():
            if marcha > self.marcha:
                print("marcha trocada para cima")
            elif marcha < self.marcha:
                print("marcha trocada para baixo")
            self.marcha = marcha

caloi = bicicleta("vermelha", "caloi 10", 1990, 500)
print(caloi.buzinar())
print(caloi.empinar())
print(caloi.trocar_marcha(3))
print(caloi.trocar_marcha(5))
