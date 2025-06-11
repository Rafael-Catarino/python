import random

# Tipos numéricos em Python
num_i = 10    # int (inteiro)
print("Valor: " + str(num_i) + " - Tipo: " + str(type(num_i)))
num_f = 5.2   # float (número decimal)
print("Valor: " + str(num_f) + " - Tipo: " + str(type(num_f)))
num_c = 1j    # complex (número complexo)
print("Valor: " + str(num_c) + " - Tipo: " + str(type(num_c)))

# Conversões entre tipos numéricos
x = int(num_f)    # Converte float para inteiro -> 5
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))
x = float(num_i)  # Converte inteiro para float -> 10.0
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))

# Criando uma lista (array) com números aleatórios entre 0 e 58
num_r = [
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
    random.randrange(0, 59),
]

print("Valor: " + str(num_r) + " - Tipo: " + str(type(num_r)))
