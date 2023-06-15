""" Precisamos criar uma função que calcule a média aritmética com a soma de três notas AV1, AV2 e AV3 para
ser utilizadoem um programa de geração automática de correção de provas. Sabe-se que apenas as duas maiores
notas das três disponíveis serão calculadas descartando a menor nota. Qual seria uma forma correta e adequada
de se definir tal função em Python? """


def get_data():
    n1 = float(input('Informe a 1ª nota: '))
    n2 = float(input('Informe a 2ª nota: '))
    n3 = float(input('Informe a 3ª nota: '))
    return pega_maior_nota(n1, n2, n3)


def pega_maior_nota(n1, n2, n3):
    maior1 = n1
    maior2 = n2
    if maior1 >= n3:
        if maior2 >= n3:
            return calcula_media(maior1, maior2)
        else:
            return calcula_media(maior1, n3)
    elif maior1 < n3:
        if maior1 <= maior2:
            return calcula_media(maior2, n3)
        else:
            return calcula_media(maior1, n3)


def calcula_media(nota1, nota2):
    result = (nota1 + nota2)/2
    return result


media = get_data()
print(media)
