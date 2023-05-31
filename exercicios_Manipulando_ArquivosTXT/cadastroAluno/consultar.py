def cabecalho():
    print("-------------------------------------")
    print("---------- Consultar Aluno ----------")
    print("-------------------------------------")


def consultaAluno():
    cabecalho()
    with open("arquivo.txt", "r") as arquivo:
        print(arquivo.read())
