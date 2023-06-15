""" Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento. """


def transforma__taxa(pais_a, taxa_pais_a, taxa_pais_b, pais_b):
    taxa_a = taxa_pais_a / 100
    taxa_b = taxa_pais_b / 100
    calcula(pais_a, taxa_a, taxa_b, pais_b)


def calcula(pais_a, taxa_a, taxa_b, pais_b):
    cont = 0
    populacao_pais_a = pais_a
    populacao_pais_b = pais_b
    while populacao_pais_a <= populacao_pais_b:
        populacao_pais_a = populacao_pais_a + (populacao_pais_a * taxa_a)
        populacao_pais_b = populacao_pais_b + (populacao_pais_b * taxa_b)
        cont += 1
    print(f"No {cont}º ano, o pais 'a' vai ter {int(populacao_pais_a)} de população e o pais 'b' vai ter"
          f"{int(populacao_pais_b)} de população.")


def start_programa():
    pais_a = 80000
    taxa_pais_a = 3
    pais_b = 200000
    taxa_pais_b = 1.5
    transforma__taxa(pais_a, taxa_pais_a, taxa_pais_b, pais_b)


start_programa()
