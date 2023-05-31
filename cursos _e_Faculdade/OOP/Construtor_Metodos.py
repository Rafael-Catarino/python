import os
os.system("clear")


class Carro:
    velMax = 0
    nome = ""
    cor = ""

    def __init__(self, velMax, nome, cor):
        self.velMax = velMax
        self.nome = nome
        self.cor = cor

    def mostrar(self):
        print("------------------------------")
        print(f"Nome: {self.nome}\nVelocidade: {self.velMax}\nCor: {self.cor}")



nomeCarro = input("Nome do carro....: ").capitalize()
velocidadeMaxima = int(input("Velocidade Maxima: "))
corCarro = input("Cor do carro.....: ").capitalize()


c1 = Carro(velocidadeMaxima, nomeCarro, corCarro)

c1.mostrar()

