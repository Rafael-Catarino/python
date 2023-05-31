import os
os.system("clear")


def header():
    print("------------------------------")
    print("      Cadastro de carros      ")
    print("------------------------------")


def menu():
    flag = "S"
    while (flag == "S"):
        print("Escolha uma opção:")
        num = int(input("""[1]Incluir Carro\n[2]Mostrar Carros\n[3]Excluir Carro\n[4]Alterar Carro\n"""))
        if num == 1:
            chooseTheBrand()
        elif num == 2:
            showCars()
        elif num == 3:
            deleteTheCar()
        elif num == 4:
            changeTheCar()
        flag = input("Deseja continuar?[S]para continuar:").upper()


header()
menu()
