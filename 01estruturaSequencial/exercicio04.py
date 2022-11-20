'''Faça um Programa que peça as 4 notas bimestrais e mostre a média.'''

num = 0
media = 0

for i in range(1, 5):
    num = float(input(f'Informe a {i}ª nota: '))
    media += num

print(media / 4)
