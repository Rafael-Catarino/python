"""Faça um programa que leia o nome a matricula e as notas do primeiro, segundo, e terceiro,
quarto semestre, calcula a media aritimetica e guarde no arquivo .TXT e por final mostre oq
 foi guardado."""
import os
os.system("cls")


def header():
    print("-------------------------------------")
    print("--------- Cadastro de Aluno ---------")
    print("-------------------------------------")


def print_list():
    print("Os alunos cadastrados foram:")
    with open("arquivo.txt", "r") as file:
        print(file.read())


def situation(average):
    if average >= 7:
        return "Aprovado"
    elif 7 > average >= 4:
        return "Recuperação"
    else:
        return "Reprovado"


def calculate_average(student):
    average = (float(student[2]) + float(student[3]) + float(student[4]) + float(student[5]))/4
    return str(average)


def save_student(student):
    with open("arquivo.txt", "a") as file:
        file.writelines([student, "\n"])


""" def validaAluno(aluno):
    print(aluno)
    resp = input("Deseja alterar alguma coisa do aluno? [digite s]:").upper()
    if resp == "S":
        os.system("clear")
        cabecalho()
        return cadastrarAluno() """


def student_registration():
    name = input("Informe o nome do aluno: ").upper()
    average = input("Informe a matricula: ")
    note1 = input("Informe a 1º nota: ")
    note2 = input("Informe a 2º nota: ")
    note3 = input("Informe a 3º nota: ")
    note4 = input("Informe a 4º nota: ")
    return [name, average, note1, note2, note3, note4]


def start_program():
    flag = "S"
    while flag == "S":
        header()
        student = student_registration()
        """ aluno = validaAluno(aluno) """
        student.append(calculate_average(student))
        student.append(situation(float(student[-1])))
        save_student(" - ".join(student))
        
        flag = input("Deseja cadastrar mais algum aluno? [Se sim digite: s]: ").upper()
        os.system("cls")
    print_list()


start_program()
