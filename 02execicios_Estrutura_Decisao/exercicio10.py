""" Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. """
import os
os.system('clear')


def get_data():
    turno = ' '
    while (turno):
        turno = input(
            'Em que turno você estuda? Dite: M-matutino ou V-Vespertino ou N- Noturno: ').upper()
        if (turno == 'M') or (turno == 'V') or (turno == 'N'):
            break
        print('Valor Inválido!')
    print_answer(turno)


def print_answer(turno):
    if turno == 'M':
        print("Bom Dia!")
    if turno == 'V':
        print("Boa Tarde!")
    if turno == 'N':
        print("Boa Noite!")


get_data()
