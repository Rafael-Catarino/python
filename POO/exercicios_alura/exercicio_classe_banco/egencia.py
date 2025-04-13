from POO.aula.exercicios_alura.exercicio_classe_banco.banco import Banco


class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero
