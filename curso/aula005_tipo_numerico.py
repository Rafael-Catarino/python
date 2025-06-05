import random

num_i = 10
num_f = 5.2
num_c = 1j
x = int(num_f) # Tranforma um numero float em int
x = float(num_i) # Tranforma um numero int em float

num_r = [ # List / Array
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
]

x = num_r


print("Valor: " + str(x) + " - Tipo:" + str(type(x)))
