# set: (conjunto) é uma coleção que não permite elementos repetidos.

# Forma incorreta de criar um set (vai dar erro):
# num = set(1, 2, 3, 1, 3, 4)

# Forma correta de criar um set usando chaves {}:
num = {1, 2, 3, 1, 3, 4, 5, 7, 9, 8, 6, 5, 1, 3, 1, 6, 1, 3}  # Elementos repetidos serão ignorados
print("Valor: " + str(num)) # Saída: {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Tipo: " + str(type(num)))

# Criando um set a partir de uma string, que cria um conjunto com caracteres únicos:
letters = set("abacaxi")
print(letters)  # Saída: {'a', 'b', 'c', 'i', 'x'}
print("Tipo: " + str(type(num)))

# Criando um set de carros (elementos repetidos são ignorados):
car = {"Palio", "Gol", "Celta", "Palio"}
print(car)  # Saída: {'Gol', 'Palio', 'Celta'}
print("Tipo: " + str(type(num)))

# OBS: Não é possível acessar elementos de um set por índice, pois sets não são ordenados.

# print(num[0])  # Isso gera erro: TypeError: 'set' object is not subscriptable

# Para acessar elementos por índice, converta o set em uma lista:
number = list(num)
print(number[0])  # Agora é possível acessar pelo índice
print("Tipo: " + str(type(num)))

# Também é possível iterar sobre um set com um loop for:
for i, c in enumerate(car):
    print(f"{i}: {c}")


# -------------- Continuação -----------------


set_a = {1, 2, 3}
set_b = {2, 3, 4}

# ---- {}.union() ---- #
# set_a.union(set_b) une os dois conjuntos, retornando todos os elementos únicos.
print(set_a.union(set_b))  # Saída: {1, 2, 3, 4}

# ---- {}.intersection() ---- #
# set_a.intersection(set_b) retorna os elementos presentes em ambos os conjuntos.
print(set_a.intersection(set_b))  # Saída: {2, 3}

# ---- {}.difference() ---- #
# set_a.difference(set_b) retorna os elementos que estão em set_a, mas não em set_b.
print(set_a.difference(set_b))  # Saída: {1}

# set_b.difference(set_a) retorna os elementos que estão em set_b, mas não em set_a.
print(set_b.difference(set_a))  # Saída: {4}

# ---- {}.symmetric_difference() ---- #
# set_a.symmetric_difference(set_b) retorna elementos que estão em set_a ou set_b, mas não em ambos (diferença simétrica).
print(set_a.symmetric_difference(set_b))  # Saída: {1, 4}

set_c = {1, 2, 3}
set_d = {4, 1, 2, 5, 6, 3}

# ---- {}.issubset() ---- #
# Retorna True se todos os elementos de set_c estiverem em set_d.
print(set_c.issubset(set_d))  # Saída: True

# Retorna False porque nem todos os elementos de set_d estão em set_c.
print(set_d.issubset(set_c))  # Saída: False

# ---- {}.issuperset() ---- #
# Retorna True se set_c contém todos os elementos de set_d.
print(set_c.issuperset(set_d))  # Saída: False

# Retorna True porque set_d contém todos os elementos de set_c.
print(set_d.issuperset(set_c))  # Saída: True

set_e = {7, 8, 9}

# ---- {}.isdisjoint() ---- #
# Retorna True se set_d e set_e não possuem elementos em comum.
print(set_d.isdisjoint(set_e))  # Saída: True

# Retorna False porque set_c e set_d possuem elementos em comum.
print(set_c.isdisjoint(set_d))  # Saída: False

# ---- Adicionando elementos ---- #
sorteio = {1, 23}
sorteio.add(25)  # Adiciona 25 ao conjunto
sorteio.add(23)  # Não altera pois 23 já existe no conjunto
print(sorteio)  # Saída: {1, 23, 25}

# ---- Limpando o conjunto ---- #
sorteio.clear()  # Remove todos os elementos do conjunto
print(sorteio)  # Saída: set()

# ---- Copiando um conjunto ---- #
a = {1, 2}
b = a.copy()  # Cópia do conjunto 'a'
print(b)  # Saída: {1, 2}

# ---- Removendo elementos ---- #
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros.discard(1)  # Remove 1 se existir, sem erro se não existir
numeros.discard(45)  # Tenta remover 45, mas não gera erro porque não existe
print(numeros)

# ---- Remover e retornar um elemento arbitrário ---- #
numeros.pop()  # Remove e retorna um elemento arbitrário do conjunto
print(numeros)

# ---- Remover elemento com erro se não existir ---- #
numeros.remove(3)  # Remove o elemento 3
# numeros.remove(60)  # Se descomentado, gera erro KeyError porque 60 não está no conjunto
print(numeros)

# ---- Tamanho do conjunto ---- #
print(len(numeros))  # Quantidade de elementos no conjunto

# ---- Verificar se elemento está no conjunto ---- #
print(7 in numeros)  # True
print(10 in numeros)  # False
