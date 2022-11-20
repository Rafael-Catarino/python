'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

nota = float(input('Informe uma nota de 1 a 10: '))
while (nota > 10 or nota < 0):
    nota = int(
        input('Você digitou uma nota invalida, favor digitar uma nota valida: '))
print(f'Você digitou a nota {nota}.')
