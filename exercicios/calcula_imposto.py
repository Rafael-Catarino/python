"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo
de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas. (0,5 ponto)."""


def soma_imposto(t, c):
    valor_imposto = t * c
    soma = c + valor_imposto
    return soma


def get_data():
    taxa_imposto = float(input('Informe um valor de taxa de imposto. Ex 10: '))
    taxa = taxa_imposto / 100
    custo = float(input('Informe o valor do custo do produto: '))
    return soma_imposto(taxa, custo)


valor = get_data()
print(f'O valor do custo com o imposto é de: R$ {valor}')
