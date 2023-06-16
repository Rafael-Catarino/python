import os

path_directory = os.path.dirname(__file__)
flag = "S"

"""w = write, a = append, r = read, x = create, b = modo binário"""

file = open(path_directory + "/file.txt", "a")
while flag == "S":
    name = input("Nome:").upper()
    file.write(name + "\n")
    flag = input("Digite 'S' para continuar: ").upper()
file.close()

file = open(path_directory + "/file.txt", "r")
print(file.read())
file.close()
