import os

path_file = os.path.dirname("__file__")


def header():
    print("-------------------------------------")
    print("----------- Alterar Aluno -----------")
    print("-------------------------------------")


def change_student_data():
    header()
    with open(path_file + "file_student_data.txt", "r") as file:
        print(file.read())
        takes_data()


def takes_data():
    line = int(input("Informe a linha que deseja alterar: "))
    wrong_data = input("Informe o dado que deseja alterar: ").upper()
    data_right = input("Informe o dado certo: ").upper()
    with open("file_student_data.txt", "r") as arquivo:
        arr_student = arquivo.readlines()
        arr_right = arr_student[line-1].replace(wrong_data, data_right)
        arr_student.pop(line-1)
        arr_student.insert(line-1, arr_right)
    with open("file_student_data.txt", "w") as arquivo:
        arquivo.writelines(arr_student)
    resp = input("Deseja alterar outra informação [s | n]: ").upper()
    if resp == "S":
        os.system("cls")
        change_student_data()
    print("As alterações foram realizadas com sucesso.")
