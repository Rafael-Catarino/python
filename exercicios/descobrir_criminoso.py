"""Utilizando LISTAS, implementar um programa em Python que faça 5 perguntas para uma
pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima ?"
b) "Esteve no local do crime ?"
c) "Mora perto da vítima ?"
d) "Devia para a vítima ?"
e) "Já trabalhou com a vítima ?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassina". Caso contrário, ela será classificada como
"Inocente"."""


listQuestions = [
    "Telefonou para a vítima ?",
    "Esteve no local do crime ?",
    "Mora perto da vítima ?",
    "Devia para a vítima ?",
    "Já trabalhou com a vítima ?"
]

res = 0

for question in listQuestions:
    answer = input(f'Você {question} Digite "S" para sim e "N" para não: ')
    while answer:
        if answer.upper() == 'N':
            break
        if answer.upper() == 'S':
            res += 1
            break
        print('Você digitou uma resposta invalida.')
        answer = input(f'Você {question} Digite "S" para sim e "N" para não: ')

if res < 2:
    print('Inocente')
elif res == 2:
    print('Suspeito')
elif 2 < res < 5:
    print('Cúmplice')
else:
    print('Assassino')
    