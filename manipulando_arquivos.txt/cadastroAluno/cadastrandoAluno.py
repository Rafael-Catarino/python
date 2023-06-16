from incluir import save_student_data
from alterar import change_student_data
from consultar import consult_student_data
from deletar import show_student_data
import os


def header():
    print("-------------------------------------")
    print("--------- Cadastro de Aluno ---------")
    print("-------------------------------------")


def start():
    resp = "S"
    while resp == "S":
        os.system("cls")
        header()
        print(
            "O que deseja fazer:\n[1]Incluir\n[2]Alterar\n[3]Deletar\n[4]Consultar ")
        flag = int(input("Informe sua opção: "))
        os.system("cls")
        if flag == 1:
            save_student_data()
        elif flag == 2:
            change_student_data()
        elif flag == 3:
            show_student_data()
        elif flag == 4:
            consult_student_data()
        resp = input("\nDeseja continuar no programa? [s|n]: ").upper()


start()
