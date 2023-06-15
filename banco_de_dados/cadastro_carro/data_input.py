from database_code import *
import os


# - Cabeçalho -#
def header():
    print("------------------------------------")
    print("-------- Cadastro de Carro ---------")
    print("------------------------------------")


def header_insert():
    print("------------------------------------")
    print("----------- Inserir Carro ----------")
    print("------------------------------------")


def header_delet():
    print("------------------------------------")
    print("---------- Excluir Carro -----------")
    print("------------------------------------")


def header_select():
    print("------------------------------------")
    print("----- Consultar Lista de Carros ----")
    print("------------------------------------")


def header_update():
    print("------------------------------------")
    print("----------- Alterar Carro ----------")
    print("------------------------------------")


# - Função para entrada de dados - #
def get_data():
    name = input("Nome..: ").upper()
    brand = input("Marca.: ").upper()
    color = input("Cor...: ").upper()
    insert_data(name, brand, color)


# - Função que mostra os dados gravados - #
def show_car_list():
    print("{:<3} | {:<10} | {:<10} | {:<10}".format("ID", "NOME", "MARCA", "COR"))
    print("------------------------------------")
    arr_car = select_car()
    for car in arr_car:
        print("{:<3} | {:<10} | {:<10} | {:<10}".format(car[0], car[1], car[2], car[3]))


# - Função que deleta um dado gravado - #
def delete_car():
    show_car_list()
    identification = input("Informe o id do carro: ")
    delete_data(identification)
    print("Carro deletado.")


# - Função que altera dado gravado - #
def update_car():
    show_car_list()
    id_car = input("Id do carro: ")
    name = input("Nome..: ").upper()
    brand = input("Marca.: ").upper()
    color = input("Cor...: ").upper()
    update_data(name, brand, color, id_car)


# - Função que escolhe o que vai ser feito - #
def choice_of_case(num):
    if num == "1":
        os.system("cls")
        header_insert()
        get_data()
    elif num == "2":
        os.system("cls")
        header_delet()
        delete_car()
    elif num == "3":
        os.system("cls")
        header_select()
        show_car_list()
    else:
        os.system("cls")
        header_update()
        update_car()


# - Função que começa o programa - #
def start_program():
    flag = "S"
    while flag == "S":
        os.system("cls")
        header()
        num = input("O que deseja fazer:\n 1 - Inserior\n 2 - Deletar\n 3 - Consultar\n 4 - Alterar\n Alunos:  ")
        while num > "4" or num < "1":
            os.system("cls")
            header()
            print("Numero invalido:")
            num = input("O que deseja fazer:\n 1 - Inserior\n 2 - Deletar\n 3 - Consultar\n 4 - Alterar\n Alunos:  ")
        choice_of_case(num)
        flag = input("Deseja continuar: [S ou N]:").upper()


start_program()
