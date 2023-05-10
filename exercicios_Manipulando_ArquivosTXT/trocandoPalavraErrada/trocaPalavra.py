"""Faça um programa que peça uma Frase ao usuário, quarde em um arquivo .txt, imprima a Frase digitada e pergunte se a tem alguma palavra errada, se tiver peça a palavra escrita certa e troca a palavra errada pela certa. """

import os
os.system("clear")


def getPhrase():
    with open("arqui1.txt", "w") as file1:
        Phrase = input("Digite uma frase: ")
        file1.write(Phrase)
    readPhrase()


def readPhrase():
    with open("arqui1.txt", "r") as file1:
        print("A frase foi:", file1.read())
    replaceWord()


def replaceWord():
    resp = input(
        "Deseja modificar alguma palavra da Frase: (Digite S para modificar)").upper()
    if resp == "S":
        errada = input("Informe a palavra errada que você quer trocar: ")
        certa = input("Informe agora a palavra certa: ")
        with open("arqui1.txt", "r") as arqui1:
            err = arqui1.read()
        with open("arqui2.txt", "w") as arqui2:
            cer = err.replace(errada, certa)
            arqui2.write(cer)
    print("Sua frase foi guardada com sucesso")
    with open("arqui2.txt", "r") as arqui2:
        print(arqui2.read())


getPhrase()
