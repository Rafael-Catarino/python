from incluir import salvaAluno
from alterar import alteraAluno
from consultar import consultaAluno
from deletar import mostraDado
import os


def cabecalho():
    print("-------------------------------------")
    print("--------- Cadastro de Aluno ---------")
    print("-------------------------------------")


def start():
    resp = "S"
    while (resp == "S"):
        os.system("clear")
        cabecalho()
        print(
            "O que deseja fazer:\n[1]Incluir\n[2]Alterar\n[3]Deletar\n[4]Consultar ")
        flag = int(input("Informe sua opção: "))
        os.system("clear")
        if flag == 1:
            salvaAluno()
        elif flag == 2:
            alteraAluno()
        elif flag == 3:
            mostraDado()
        elif flag == 4:
            consultaAluno()
        resp = input("\nDeseja continuar no programa? [s|n]: ").upper()


start()
