# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor


class Bola:
    cor = 'VERMELHA'
    circunf = 15
    material = 'PLASTICO'

    def __init__(self, color, circunf, material):
        self.cor = color
        self.circunf = circunf
        self.material = material

    def informe_cor(self):
        input_cor = input("Digite uma cor: ")
        self.cor = input_cor

    def informe_cricunf(self):
        input_circunf = input("Digite a circunferencia da bola: ")
        self.circunf = input_circunf

    def informe_material(self):
        input_material = input("Digite qual o material: ")
        self.material = input_material

    def troca_cor(self):
        troca = input(f"Deseja mudar a cor atual? (S/N): ")

        troca = troca.upper()

        if troca == "S":
            nova_cor = input("Digite a cor que você deseja: ")
            self.cor = nova_cor
        else:
            print(f'Tudo bem a cor continua sendo {self.cor}')

    def mostra_cor(self):
        print(f'A cor da bola é: {self.cor}')


def criando_bola():
    bola1 = Bola("VERMELHA", 15, "PLASTICO")
    while True:
        bola1.informe_cor()
        bola1.informe_cricunf()
        bola1.informe_material()
        bola1.mostra_cor()
        bola1.troca_cor()

        continuar = input("Continuar? [s/n]").lower()
        if continuar == "n":
            break

    bola1.mostra_cor()
    print(
        f"A cor da bola é: {bola1.cor}, A circunferência da bola é: {bola1.circunf}, O matérial da bola é: {bola1.material}")


criando_bola()
