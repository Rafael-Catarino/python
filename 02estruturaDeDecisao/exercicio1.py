"""Faça um Programa que peça dois números e imprima o maior deles."""
import os
os.system('clear')


def print_bigger_number(num1, num2):
    if num1 > num2:
        print(f"O número maior foi o: {num1}, o primeiro número informado.")
    else:
        print(f"O número mair foi o: {num2}, o segundo número informado.")


def get_number():
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))
    print_bigger_number(num1, num2)


get_number()
