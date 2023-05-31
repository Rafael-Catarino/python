from delete_record_in_table import insert_data
import os

os.system("cls")

def header():
    print("--------------------------------")
    print("----------- Cadastro -----------")
    print("--------------------------------")



def register():
    header()
    for i in range(0, 2):
        name = input("Nome....: ")
        telphone = input("Telefone: ")
        email = input("E-mail..: ")
        insert_data(name, telphone, email)
        print("--------------------------------")


register()