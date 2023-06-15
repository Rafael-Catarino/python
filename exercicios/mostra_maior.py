"""Faça um Programa que leia três números e mostre o maior deles."""


def get_number():
    number = []
    for i in range(1, 4):
        number.append(float(input(f"Informe o {i}º número: ")))
    print_bigger_number(number)


def print_bigger_number(num):
    if num[0] > num[1] and num[0] > num[2]:
        print(f"O número maior foi o {num[0]}")
    elif num[1] > num[0] and num[1] > num[2]:
        print(f"O numero maior foi o {num[1]}")
    elif num[2] > num[0] and num[2] > num[1]:
        print(f"O numero maioe foi o {num[2]}")


get_number()
