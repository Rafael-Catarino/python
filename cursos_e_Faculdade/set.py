# Um set é uma coleção que não possui objetos repitidos.

# num = set(1, 2, 3, 1, 3, 4) outra forma de criar um conjunto(set)
num = {1, 2, 3, 1, 3, 4}
print(num)

letters = set("abacaxi")
print(letters)

# car = set(("Palio", "Gol", "Celta", "Palio"))
car = {"Palio", "Gol", "Celta", "Palio"}
print(car)

# OBS: Para eu consegui acessar um elemanto no meu set, eu preciso transformar ele em uma lista.

# print(num[0]) Essa linha da um erro.
number = list(num)
print(number[0])

# Já da para interar o set com um for.
for i, c in enumerate(car):
    print(f"{i}: {c}")

