import os


def header():
    print("-------------------------------------")
    print("---------- Cadastrar Aluno ----------")
    print("-------------------------------------")


""" def contaLinhas():
    with open("arquivo.txt", "r") as arquivo:
        return len(arquivo.readlines())+1 """


def save_student_data():
    flag = "S"
    while flag == "S":
        header()
        """ linha = str(contaLinhas()) """
        nome = input("Nome: ").upper()
        mat = input("Matricula: ")
        nota1 = input("1º Nota: ")
        nota2 = input("2º Nota: ")
        nota3 = input("3º Nota: ")
        nota4 = input("4º Nota: ")
        arr = [nome, mat, nota1, nota2, nota3, nota4]
        path_file = os.path.dirname(__file__)
        with open(path_file + "/file_student_data.txt", "a") as file:
            file.writelines([" - ".join(arr), " - \n"])
        print("O aluno foi salvo com sucesso.")
        flag = input("Incluir novo aluno [s | n]? ").upper()        
