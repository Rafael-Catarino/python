from abc import ABC, abstractclassmethod


class Veiculo(ABC):

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f"{self.marca} | {self.modelo} | {status}"

    @abstractclassmethod
    def ligar(sel):
        pass


# carro = Veiculo("Fiat", "Uno")


# def main():
#     print(carro)


# if __name__ == "__main__":
#     main()
