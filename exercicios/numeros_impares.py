"""Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."""

y = 1

while y < 50:
    print(y)
    y += 2

print('------SEGUNDA FORMA...------')

for x in range(1, 50, 2):
    print(x)
