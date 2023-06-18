"""Faça um programa que peça ao usuário o seu nome e a sua idade,
crie um arquivo .txt e guarde nesse arquivo os dados solicitados ao usuário. """

import metodos as metodos
import os
os.system("cls")

""" arquivo = open("arquivo.txt", "x") Cria um aquivo.txt  """


def create_list():
    file = open("./manipulandoArquivosTXT/nomeIdade/listaNomeIdade.txt", "a")
    flag = ""
    while flag != "-1":
        name = metodos.get_name()
        age = metodos.get_old()
        pessoa = [name, " ", age, "\n"]
        file.writelines(pessoa)
        flag = input("Para terminar o programa digite: [-1] ").upper()
    file.close()
    file = open("./manipulandoArquivosTXT/nomeIdade/arquivo.txt", "r")
    print(file.read())


create_list()
