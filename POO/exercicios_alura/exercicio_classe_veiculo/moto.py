from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f"{self.marca} | {self.modelo} - tipo: {self.tipo} - Status: {status}"

    def ligar(self):
        pass
