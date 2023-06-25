class Carro:
    # atributos
    chassi = 000000000000
    cor = 1
    motor = 2.0
    litros = 0

    # constructor
    def __init__(self, chassi, cor, motor, litros):
        self.chassi = chassi
        self.cor = cor
        self.motor = motor
        self.litros = litros
    # métodos

    def ligar(self):
        print("Carro ligado...")

    def tem_gasolina(self):
        if self.litros > 0:
            return True
        else:
            return False


carro1 = Carro('9ASWX000001', 2, 1.8, 0)

print('Chassi: ', carro1.chassi)
print('Cor: ', ('Azul' if carro1.cor == 1 else 'Branco'))
print("Motor: ", carro1.motor)

if carro1.tem_gasolina():
    carro1.ligar()
else:
    print('Precisa abastecer')
