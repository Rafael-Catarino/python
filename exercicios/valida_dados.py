""" Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; """
import os
os.system('clear')


def get_name():
    nome = input('Digite seu nome: Min 3 caracteres: ').upper()
    while len(nome) < 3:
        print('Não pode ser um nome com menos de 3 caracteres. Favor digitar outro nome.')
        nome = input('Digite seu nome: Min 3 caracteres: ').upper()
    os.system('clear')
    return nome


def get_idade():
    idade = int(input('Digite sua idade: '))
    while idade < 0 or idade > 150:
        print('Idade invalida, favor digite uma idade entre 0 e 150.')
        idade = int(input('Digite sua idade: '))
    os.system('clear')
    return idade


def get_salario():
    salario = float(input('Informe o salário: R$:  '))
    while salario < 0:
        print('Salário invalido. Favor informar um salário maior que 0.')
        salario = float(input('Informe o salário: R$: '))
    os.system('clear')
    return salario


def get_sexo():
    sexo = input('Digite seu Sexo: M e F ').upper()
    while sexo != 'M' and sexo != 'F':
        print("Sexo errado. Favor digitar 'M' para masculino ou 'F' para feminino")
        sexo = input('Digite seu Sexo: M e F ').upper()
    os.system('clear')
    return sexo


def get_estado_civil():
    estado_civil = input(
        "Digite seu Estado Civil: 'S', 'C', 'V', 'D': ").upper()
    while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
        print("Estado Civil. Favor digitar 'S' para Solteiro, 'C' para Casado, 'V' Viuvo ou 'D' Divorciado.")
        estado_civil = input(
            "Digite seu Estado Civil: 'S', 'C', 'V', 'D': ").upper()
    os.system('clear')
    return estado_civil


def print_data():
    print(f'Nome: {get_name()}, \nIdade: {get_idade()}, \nSalario: {get_salario()},'
          f' \nSexo: {get_sexo()}, \nEstado Civil: {get_estado_civil()}')


print_data()
