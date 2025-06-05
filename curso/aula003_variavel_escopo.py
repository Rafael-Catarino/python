# variavel global
num1=num2=num3=0


def cn():
    # variavel local
    teste1 = "Foi"
    print(teste1)

    # declarei minha variavel como global.
    global canal 
    canal = "CFB Cursos"

cn()

# print(teste1)  Nesse caso da erro pq a variavel teste1 não está no escopo de global e sim no escopo local.

print(canal) # Nesse caso não vai dar erro pos a variavel canal está no escopo global.