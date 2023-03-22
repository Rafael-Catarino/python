""" Considere uma lista em Python como lista = [1, 2, 4, -5, 7, -9]. Escreva um trecho de código que retorne apenas os
elementos negativos da lista. """

lista = [1, 2, 4, -5, 7, -9]

for num in lista:
    if num < 0:
        print(num)