# Declaração de variável global.
num1=num2=num3=0


def cn():
    # Declaração de variável local.
    teste1 = "Foi"
    print(teste1)

    # Declaração de variável global.
    global canal 
    canal = "CFB Cursos"

cn()

# print(teste1) Erro causado pelo uso da variável 'teste1' fora do seu escopo local.
# Para acessá-la globalmente, seria necessário declará-la como global.

print(canal) # Como 'canal' é uma variável global, pode ser utilizada e modificada 
# em qualquer parte do programa (inclusive dentro de funções, caso seja declarada com 'global').
