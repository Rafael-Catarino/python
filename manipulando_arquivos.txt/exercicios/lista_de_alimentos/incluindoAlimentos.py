"""Faça um programa que peça ao usuario um alimento, crie um arquivo .txt,
uarde esse alimento no aquivo, pergunte se ele quer guardar novos alimentos
e ao final imprima a lista de alimentos."""

import os

os.system("cls")
path_file = os.path.dirname(__file__)


flag = ""
with open(path_file + "/listaDeAlimentos.txt", "a") as file:
    while flag != "n":
        alimento = input("Informe um alimento: ").upper()
        file.writelines([alimento, "\n"])
        flag = input("Deseja continuar?")
        os.system("cls")

with open(path_file + "/listaDeAlimentos.txt", "r") as file:
    print(file.read())
