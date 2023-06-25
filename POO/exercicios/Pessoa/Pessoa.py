# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.


class Pessoa:
    nome = ''
    idade = 0
    peso = 0.0
    altura = 0.0

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def fica_mais_velho(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.05

    def emgordar_ou_emagrecer(self):
        flag = input(
            f"Você está pesando {self.peso}Kg deseja mudar o peso? [s/n]: ").lower()

        if flag == "s":
            novo_peso = input("Digite seu novo peso: ")
            self.peso = novo_peso
            print(f"Seu novo peso é: {self.peso}Kg")
        else:
            print(f"Seu peso continua {self.peso}Kg")


n = input("Informe seu nome: ")
i = input("Informe sua idade: ")
p = input("Informe o seu peso: ")
a = input("Informe sua altura: ")


pessoa1 = Pessoa(n, i, p, a)
print(f"nome: {pessoa1.nome}, idade: {pessoa1.idade}, peso: {pessoa1.peso} e altura: {pessoa1.altura}.")

pessoa1.emgordar_ou_emagrecer()
