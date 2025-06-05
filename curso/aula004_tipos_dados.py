x = 1 # int
x = "CFB Curso" # string
x = 3.6 # float
x = True # bool

x = ["Carro", "Avião", "Navio", 1, 58.3, True] # list
x[3] = "Bicicleta" 
x = ("Carro", "Avião", "Navio", 1, 58.3, True) # Tupla - Igual a list porem não consigo modificar as coisa de dentro dela.
# EX: x[3] = "Bicicleta" se eu rodar esse codigo vai dar um erro, pos estou tentando alterar um componente de uma tupla.

x = range(0,100,2) # cria uma lista de 0 a 100 de 2 em 2 números.
x = { # Dictionare.
    "canal" : "CFB Cursos",
    "curso" : "Curso de Python",
    "nome" : "Rafael",
}

x = {5,7,9,8,6,5,1,3,1,6,1,3} # Set não repete valores.


print("Valor: " + str(x))
print("Tipo: " + str(type(x)))