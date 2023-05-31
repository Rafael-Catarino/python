""" Faça um programa que leia 5 números e informe a soma e a média dos números. """

soma = 0
media = 0
for x in range(1, 6):
    num = int(input(f'Informe o {x}º número: '))
    soma += num
    media = soma/5
print(f'A Soma é: {soma} e a Média é: {media}.')
