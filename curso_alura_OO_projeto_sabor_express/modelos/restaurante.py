from modelos.avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False  # O _ faz com que esse atributo fique privado.
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
        print(
            f"{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}")
        print("-" * 80)
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print("Favor informar um valor menor que 5")

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "Restaurante sem avalição"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

# restaurante_praca = Restaurante("Praça", "Gourmet")
# restaurante_praca.alternar_estado()
# restaurante_pizza = Restaurante("Pizza Express", "Italiana")

# Restaurante.listar_restaurantes()

# print(restaurante_praca)
# print(restaurante_pizza)
# print(vars(restaurante_praca))
# print(dir(restaurante_praca))
