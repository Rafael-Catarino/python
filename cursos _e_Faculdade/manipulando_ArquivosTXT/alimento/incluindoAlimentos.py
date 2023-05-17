"""Faça um programa que peça ao usuario um alimento, crie um arquivo .txt, guarde esse alimento no aquivo, pergunte se ele quer guardar novos alimentos e ao final imprima a lista de alimentos."""

import os

os.system("clear")

flag=""
with open("./manipulandoArquivosTXT/alimento/listaDeAlimentos.txt", "a") as lista:
  while(flag != "n"):
    alimento = input("Informe um alimento: ").upper()
    lista.writelines([alimento, "\n"])
    flag = input("Deseja continuar?")
    os.system("clear")

lista=open("./manipulandoArquivosTXT/alimento/listaDeAlimentos.txt", "r")
print(lista.read())


