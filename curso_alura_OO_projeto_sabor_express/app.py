from modelos.restaurante import Restaurante


restaurante_praca = Restaurante("praca", "Gourmet")
restaurante_praca.receber_avaliacao("Linda", 4)
restaurante_praca.receber_avaliacao("Lais", 4)
restaurante_praca.receber_avaliacao("emy", 5)
restaurante_praca.alternar_estado()
restaurante_praca.media_avaliacoes


def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
