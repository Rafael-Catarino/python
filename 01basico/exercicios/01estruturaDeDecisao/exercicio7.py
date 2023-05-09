"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

arrNumber = []

for x in range(1, 4):
    num = int(input(f"Informe o {x}º número: "))
    arrNumber.append(num)

if arrNumber[0] > arrNumber[1] and arrNumber[0] > arrNumber[2]:
    print(f"O maior número é: {arrNumber[0]}")
elif arrNumber[1] > arrNumber[0] and arrNumber[1] > arrNumber[2]:
    print(f"O maior número é: {arrNumber[1]}")
elif arrNumber[2] > arrNumber[0] and arrNumber[2] > arrNumber[1]:
    print(f"O maior número é: {arrNumber[2]}")

if arrNumber[0] < arrNumber[1] and arrNumber[0] < arrNumber[2]:
    print(f"O menor número é: {arrNumber[0]}")
elif arrNumber[1] < arrNumber[0] and arrNumber[1] < arrNumber[2]:
    print(f"O menor número é: {arrNumber[1]}")
elif arrNumber[2] < arrNumber[0] and arrNumber[2] < arrNumber[1]:
    print(f"O menor número é: {arrNumber[2]}")
