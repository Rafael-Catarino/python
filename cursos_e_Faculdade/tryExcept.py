"""Tratamento de erro"""
try:
    print(x)
except:
    print("X não definido")
else:
    print("Tudo certo")
finally:
    print("Fim do tratamento")

num2 = 10

if not type(num2) is int:
    raise Exception("Somente numeros permitidos")
else:
    print(num2)

""" num = -10

if num < 1:
    raise Exception("Valor não permitido") """
