""" Faça um programa que receba dois números inteiros e gere os números inteiros que
 estão no intervalo compreendido por eles. """

num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe outro número inteiro: '))

if num1 > num2:
    num1, num2 = num2, num1

for x in range(num1+1, num2):
    print(x)
