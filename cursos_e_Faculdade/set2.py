set_a = {1, 2, 3}
set_b = {2, 3, 4}

# ----{}.union---- #
# set_a.union(set_b) une os dois conjuntos.
print(set_a.union(set_b))

# ----{}.intersection---- #
# set_a.intersection(set_b) mostra os elementos que tem no A e tem no B.
print(set_a.intersection(set_b))

# ----{}.diference---- #
# set_a.difference(set_b) mostra os elementos que tem no A e não tem no B.
print(set_a.difference(set_b))
# Já o set_b.difference(set_a) mostra os elementos que tem no B e não tem no A.
print(set_b.difference(set_a))

# ----{}.symmetric_diferance---- #
# set_a.symmetric_diferance(set_b) só mostra os elementos que não estão na interseção.
print(set_a.symmetric_difference(set_b))

set_c = {1, 2, 3}
set_d = {4, 1, 2, 5, 6, 3}

# ----{}.issubset---- #
# Retorna True se todos os elementos de um conjunto pertencer ao outro.
print(set_c.issubset(set_d))
# Se não pertencer retorna falso.
print(set_d.issubset(set_c))

# ----{}.issuperst---- #
# É parecido com o .issubset, porém ele troca a ordem da saída.
print(set_c.issuperset(set_d))

print(set_d.issuperset(set_c))

set_e = {7, 8, 9}
# ----{}.isdisjoint---- #
print(set_d.isdisjoint(set_e))

print(set_c.isdisjoint(set_d))

# Adiciona um elemento no set se ele não existir
sorteio = {1, 23}

sorteio.add(25)
sorteio.add(23)

print(sorteio)

# limpa o set
sorteio.clear()

print(sorteio)

# copia um set
a = {1, 2}

a.copy()

print(a)

# descarta um valor
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)

# tira sempre o primeiro valor do set
numeros.pop()

print(numeros)

# discarta um valor. Se não tiver o valor, da um erro
numeros.remove(3)
# numeros.remove(60) da um error.

print(numeros)

# retorna o tamenho do conjunto.
print(len(numeros))

# retorna se há ou não o valor no conjunto.
print(7 in numeros)
print(10 in numeros)
