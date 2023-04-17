def cabecalho():
    print("-------------------------------------")
    print("----------- Deletar Aluno -----------")
    print("-------------------------------------")


def mostraDado():
    with open("arquivo.txt", "r") as arquivo:
        print(arquivo.read())
        deletaAluno()


def deletaAluno():
    resp = int(input("Qual linha deseja deletar: "))
    with open("arquivo.txt", "r") as arquivo:
        arrAluno = arquivo.readlines()
        arrAluno.pop(resp-1)
    with open("arquivo.txt", "w") as arquivo:
        arquivo.writelines(arrAluno)
    print("O aluno foi apagado com sucesso.")