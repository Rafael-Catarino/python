"""Faça um programa que peça uma Frase ao usuário, quarde em um arquivo .txt,
imprima a Frase digitada e pergunte se a frase tem alguma palavra errada, se tiver
peça a palavra escrita certa e troca a palavra errada pela certa. """

import os
os.system("cls")


def get_phrase():
    with open("arqui1.txt", "w") as file1:
        phrase = input("Digite uma frase: ")
        file1.write(phrase)
    read_phrase()


def read_phrase():
    with open("arqui1.txt", "r") as file1:
        print("A frase foi:", file1.read())
    replace_word()


def replace_word():
    resp = input(
        "Deseja modificar alguma palavra da Frase: (Digite S para modificar)").upper()
    if resp == "S":
        wrong = input("Informe a palavra errada que você quer trocar: ")
        right = input("Informe agora a palavra certa: ")
        with open("arqui1.txt", "r") as file1:
            err = file1.read()
        with open("arqui2.txt", "w") as file2:
            cer = err.replace(wrong, right)
            file2.write(cer)
    print("Sua frase foi guardada com sucesso")
    with open("arqui2.txt", "r") as file2:
        print(file2.read())


get_phrase()
