"""Faça um programa que leia o nome a matricula e as notas do primeiro, segundo, e terceiro, quarto semestre, calcula a media aritimetica e guarde no arquivo .TXT e por final mostre oq foi guardado."""
import os
os.system("clear")

def cabecalho():
    print("-------------------------------------")
    print("--------- Cadastro de Aluno ---------")
    print("-------------------------------------")


def printLista():
    print("Os alunos cadastrados foram:")
    with open("arquivo.txt", "r") as arquivo:
        print(arquivo.read())


def aprovOuReprov(media):
    if media >= 7:
        return "Aprovado"
    elif media < 7 and media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"



def calculaMedia(aluno):
    media = (float(aluno[2]) + float(aluno[3]) + float(aluno[4]) + float(aluno[5]))/4
    return (str(media))



def guardaAluno(aluno):
    with open("arquivo.txt", "a") as arquivo:
        arquivo.writelines([aluno, "\n"])


""" def validaAluno(aluno):
    print(aluno)
    resp = input("Deseja alterar alguma coisa do aluno? [digite s]:").upper()
    if resp == "S":
        os.system("clear")
        cabecalho()
        return cadastrarAluno() """


def cadastrarAluno():
    nome = input("Informe o nome do aluno: ")
    matricula = input("Informe a matricula: ")
    nota1 = input("Informe a 1º nota: ")
    nota2 = input("Informe a 2º nota: ")
    nota3 = input("Informe a 3º nota: ")
    nota4 = input("Informe a 4º nota: ")
    return [nome, matricula, nota1, nota2, nota3, nota4]



def startPrograma():
    flag = "S"
    while(flag == "S"):
        cabecalho()
        aluno = cadastrarAluno()
        """ aluno = validaAluno(aluno) """
        aluno.append(calculaMedia(aluno))
        aluno.append(aprovOuReprov(float(aluno[-1])))
        guardaAluno(" - ".join(aluno))
        
        flag = input("Deseja cadastrar mais algum aluno? [Se sim digite: s]: ").upper()
        os.system("clear")
    printLista()


startPrograma()
