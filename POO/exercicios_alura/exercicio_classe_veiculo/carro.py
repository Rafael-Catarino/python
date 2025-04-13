from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
        super().__init__(marca, modelo)
        self.portas = portas
        self.cor = cor

    def __str__(self):
        status = "Ligado" if self._ligado else "Deligado"
        return f"{self.marca} | {self.modelo} - Portas: {self.portas} - {status} - Cor: {self.cor}"

    @property
    def listar_carro(self):
        status = "Ligado" if self._ligado else "Deligado"
        print(f"{self.marca.ljust(10)} | {self.modelo.ljust(10)} | Portas: {str(self.portas).ljust(10)} | {status.ljust(10)} | {self.cor.ljust(10)}")

    def ligar(self):
        print(f"O carro {self.modelo} está ligado.")
