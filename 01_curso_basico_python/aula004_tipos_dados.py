x = 1  # int (inteiro)]
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))

x = "CFB Curso"  # string (texto)
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))

x = 3.6  # float (número decimal)
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))

x = True  # bool (booleano)
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))

# Lista: coleção ordenada e mutável que pode conter elementos de tipos diferentes
x = ["Carro", "Avião", "Navio", 1, 58.3, True]
x[3] = "Bicicleta"  # Alterando o quarto elemento da lista (índice 3)
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))

# Tupla: coleção ordenada e imutável; não é possível alterar seus elementos após a criação
x = ("Carro", "Avião", "Navio", 1, 58.3, True)
# Exemplo que causaria erro:
# x[3] = "Bicicleta"  # Erro: 'tuple' object does not support item assignment
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))

# Range: gera uma sequência numérica (iterador) de start até stop (exclusive), com passo step
# Aqui, gera números pares de 0 até 98
x = range(0, 100, 2)  # Criando um iterador que gera números de 0 a 98, de 2 em 2
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))

# Dicionário: coleção de pares chave-valor, onde as chaves são únicas
x = {
    "canal": "CFB Cursos",
    "curso": "Curso de Python",
    "nome": "Rafael",
}
print("Valor: " + str(x))
print("Tipo: " + str(type(x)))
