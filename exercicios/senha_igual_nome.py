""" Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
 igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """
import os
os.system('clear')


def login():
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    while senha == nome:
        print('Você digitou uma senha igual ao seu nome. Favor digitar uma senha diferente do nome.')
        nome = input('Digite seu nome: ')
        senha = input('Favor digitar outra senha: ')


login()
