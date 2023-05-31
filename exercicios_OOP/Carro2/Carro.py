carros = []


class Carro():
    nome = ""
    cor = ""
    placa = 0
    ligado = False
    pot = 0
    velMax = int(pot)*2

    def __init__(self, nome, cor, placa, pot):
        self.nome = nome
        self.cor = cor
        self.placa = placa
        self.pot = pot

    def ligar():
        self.ligado = True

    def desligar():
        self.ligado = False

    def inform(self):
        print(f"""Nome: {self.nome}\nCor: {self.cor}\n""")
