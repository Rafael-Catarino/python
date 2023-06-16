import os

path_directory = os.path.dirname(__file__)

flag = "S"

with open(path_directory + "/file.txt", "a") as file:
    while flag == "S":
        name = input("Nome....:").upper()
        tel = input("Telefone:")
        file.writelines(["Nome: " + name, " Telefone: " + tel, "\n"])
        flag = input("Digite 'S' para continuar: ").upper()

with open(path_directory + "/file.txt", "r") as file:
    print(file.read())
