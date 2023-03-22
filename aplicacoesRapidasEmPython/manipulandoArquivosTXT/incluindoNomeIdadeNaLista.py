import metodos
import os
os.system("clear")

#arquivo = open("arquivo.txt", "x") Cria um aquivo.txt 


def create__List():
    file = open("./manipulandoArquivosTXT/arquivo.txt", "a") #Sobre
    flag = ""
    while (flag != "-1"):
        name = metodos.get__name()
        age = metodos.get__old()
        pessoa = [name, " ", age, "\n"]
        file.writelines(pessoa)
        flag = input("Para terminar o programa digite: [-1] ").upper()
    file.close()
    file = open("./manipulandoArquivosTXT/arquivo.txt", "r")
    print(file.read())

create__List()
