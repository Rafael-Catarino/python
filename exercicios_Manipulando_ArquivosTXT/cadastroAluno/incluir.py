import os


def cabecalho():
    print("-------------------------------------")
    print("---------- Cadastrar Aluno ----------")
    print("-------------------------------------")


def aprovOureprov(media):
    if float(media) >= 7:
        return "APROVADO"
    elif float(media) > 4:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"


def calculaMedia(nota1, nota2, nota3, nota4):
    media = (float(nota1) + float(nota2) + float(nota3) + float(nota4))/4
    return media


""" def contaLinhas():
    with open("arquivo.txt", "r") as arquivo:
        return len(arquivo.readlines())+1 """


def salvaNoarquivo(arr):
    with open("arquivo.txt", "a") as arquivo:
        arquivo.writelines([" - ".join(arr), "\n"])


def salvaAluno():
    flag = "S"
    while flag == "S":
        os.system("clear")
        cabecalho()
        """ linha = str(contaLinhas()) """
        nome = input("Nome: ").upper()
        mat = input("Matricula: ")
        nota1 = input("1º Nota: ")
        nota2 = input("2º Nota: ")
        nota3 = input("3º Nota: ")
        nota4 = input("4º Nota: ")
        media = str(calculaMedia(nota1, nota2, nota3, nota4))
        resp = aprovOureprov(media)
        arr = [nome, mat, nota1, nota2, nota3, nota4, media, resp]
        salvaNoarquivo(arr)
        print("O aluno foi salvo com sucesso.")
        flag = input("Incluir novo aluno [s | n]? ").upper()        
