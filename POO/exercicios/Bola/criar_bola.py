from Bola import Bola
import os


def cabecalho():
    print("------------------------------")
    print("         Criando a Bola       ")
    print("------------------------------")


def criando_bola():
    bola1 = Bola("VERMELHA", 15, "PLASTICO")
    while True:
        os.system("cls")
        cabecalho()
        bola1.informe_cor()
        bola1.informe_cricunf()
        bola1.informe_material()
        print("------------------------------")
        bola1.mostra_cor()
        bola1.troca_cor()

        continuar = input("Continuar? [s/n]").lower()
        if continuar == "n":
            break

    bola1.mostra_cor()
    print(
        f"A cor da bola é: {bola1.cor}, A circunferência da bola é: {bola1.circunf},"
        f"O matérial da bola é: {bola1.material}")


criando_bola()
