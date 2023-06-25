import os
os.system("cls")


class Car:
    vel_max = 0
    name = ""
    color = ""
    ligado = False

    def __init__(self, vel_max, name, color):
        self.vel_max = vel_max
        self.name = name
        self.color = color

    def mostrar(self):
        print("------------------------------")
        estado = "Sim" if self.ligado else "Não"
        print(f"Nome: {self.name}\nVelocidade: {self.vel_max}\nCor: {self.color}\nLigado: {estado}")

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if self.ligado:
            print("Estado: carro andando")
        else:
            print("Estado: carro desligado")


name_car = input("Nome do carro....: ").upper()
try:
    velocidade_maxima = int(input("Velocidade Maxima: "))
except ValueError as error:
    velocidade_maxima = int(input("Digite um valor valido:"))
color_car = input("Cor do carro.....: ").upper()

c1 = Car(velocidade_maxima, name_car, color_car)
c1.ligar()
c1.mostrar()
c1.andar()
c1.desligar()
c1.mostrar()
c1.andar()
