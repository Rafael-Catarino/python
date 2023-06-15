from inserting_record_into_table import inserting_record_into_table
import os
os.system("cls")


def header():
    print("--------------------------------")
    print("----------- Cadastro -----------")
    print("--------------------------------")


def register():
    header()
    for i in range(0, 1):
        name = input("Nome....: ")
        telphone = input("Telefone: ")
        email = input("E-mail..: ")
        inserting_record_into_table(name, telphone, email)
        print("--------------------------------")


register()
