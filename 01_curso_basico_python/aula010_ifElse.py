# Programa que pede dois números e imprime o maior deles.

import os
os.system('cls')  # Limpa o terminal (em sistemas Unix). Para Windows, use 'cls'

def print_bigger_number(num1, num2):
    if num1 > num2:
        print(f"O número maior foi: {num1} (primeiro número informado).")
    elif num2 > num1:
        print(f"O número maior foi: {num2} (segundo número informado).")
    else:
        print("Os dois números são iguais.")

def get_numbers():
    while True:
        try:
            num1 = int(input("Informe o primeiro número: "))
            num2 = int(input("Informe o segundo número: "))
            print_bigger_number(num1, num2)
            break  # Sai do loop se tudo der certo
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")
            os.system('cls')

get_numbers()