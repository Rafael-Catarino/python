'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valPorHora = float(input('Informe quanto você ganha por hora:'))
horastrabalhada = float(input('Informe o número de horas trabalhadas no mês:'))
totalSal = valPorHora * horastrabalhada

print(f'Seu sálario total será de: {totalSal:,.2f}')
