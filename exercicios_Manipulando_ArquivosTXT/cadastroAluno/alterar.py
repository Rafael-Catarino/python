import os


def cabecalho():
    print("-------------------------------------")
    print("----------- Alterar Aluno -----------")
    print("-------------------------------------")


def alteraAluno():
    cabecalho()
    with open("arquivo.txt", "r") as arquivo:
        print(arquivo.read())
        pegaDado()


def pegaDado():
    linha = int(input("Informe a linha que deseja alterar: "))
    dadoErrado = input("Informe o dado que deseja alterar: ").upper()
    dadoCerto = input("Informe o dado certo: ").upper()
    with open("arquivo.txt", "r") as arquivo:
        arrAluno = arquivo.readlines()
        arrCerto = arrAluno[linha-1].replace(dadoErrado, dadoCerto)
        arrAluno.pop(linha-1)
        arrAluno.insert(linha-1, arrCerto)
    with open("arquivo.txt", "w") as arquivo:
        arquivo.writelines(arrAluno)
    resp = input("Deseja alterar outra informação [s | n]: ").upper()
    if resp == "S":
        os.system("clear")
        alteraAluno()
    print("As alterações foram realizadas com sucesso.")
