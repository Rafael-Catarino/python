def header():
    print("-------------------------------------")
    print("----------- Deletar Aluno -----------")
    print("-------------------------------------")


def show_student_data():
    header()
    with open("file_student_data.txt", "r") as arquivo:
        print(arquivo.read())
        delet_student()


def delet_student():
    resp = int(input("Qual linha deseja deletar: "))
    with open("file_student_data.txt", "r") as arquivo:
        arr_student = arquivo.readlines()
        arr_student.pop(resp-1)
    with open("file_student_data.txt", "w") as arquivo:
        arquivo.writelines(arr_student)
    print("O aluno foi apagado com sucesso.")
