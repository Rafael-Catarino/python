"""Faça um programa que peça ao usuário o seu nome e a sua idade, crie um arquivo .txt e guarde nesse arquivo os dados solicitados ao usuário. """

import metodos as metodos
import os
os.system("clear")

""" arquivo = open("arquivo.txt", "x") Cria um aquivo.txt  """


def create__List():
    file = open("./manipulandoArquivosTXT/nomeIdade/listaNomeIdade.txt", "a") #Sobre
    flag = ""
    while (flag != "-1"):
        name = metodos.get__name()
        age = metodos.get__old()
        pessoa = [name, " ", age, "\n"]
        file.writelines(pessoa)
        flag = input("Para terminar o programa digite: [-1] ").upper()
    file.close()
    file = open("./manipulandoArquivosTXT/nomeIdade/arquivo.txt", "r")
    print(file.read())

create__List()
