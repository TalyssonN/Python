class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, valor):
        super().__init__(marca, modelo, ano)
        self.cor = cor
        self.valor = valor

    def buzinar(self):
        return "Buzina: Beep Beep!"

    def ligar(self):
        return "O carro está ligado."

    def desligar(self):
        return "O carro está desligado."
    
# Exemplo de uso da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020, "prata", 80000)
print(meu_carro.ligar())
print(meu_carro.buzinar())

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, valor):
        super().__init__(marca, modelo, ano)
        self.cor = cor
        self.valor = valor

    def acelerar(self):
        return "A moto está acelerando."

    def frear(self):
        return "A moto está freando."

    def empinar(self):
        return "A moto está empinando."
    
    def ligarMoto(self):
        return "A moto está ligada."

# Exemplo de uso da classe Moto
minha_moto = Moto("Honda", "CB500", 2021, "vermelha", 30000)

print(minha_moto.ligarMoto())
print(minha_moto.acelerar())
print(minha_moto.frear())
print(minha_moto.empinar())
