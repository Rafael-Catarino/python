"""Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

sex = input("Digite F para Feminino ou M para masculino: ")

while sex:
    if sex.upper() == "F":
        print("Feminino")
        break
    elif sex.upper() == "M":
        print("Masculino")
        break
    else:
        print("Sexo invalido")
    sex = input("Digite F para Feminino ou M para masculino: ")
