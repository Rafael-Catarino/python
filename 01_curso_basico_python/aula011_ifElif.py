# Programa que verifica se a letra digitada é "F" ou "M".
# Conforme a letra, exibe: "F - Feminino", "M - Masculino" ou "Sexo Inválido".

sex = input("Digite F para Feminino ou M para Masculino: ")

while sex:
    if sex.upper() == "F":
        print("Feminino")
        break
    elif sex.upper() == "M":
        print("Masculino")
        break
    else:
        print("Sexo Inválido")
    sex = input("Digite F para Feminino ou M para Masculino: ")


# Programa de Escolha de Passeio Conforme Clima e Dinheiro
# O programa pergunta o clima e a quantidade de dinheiro que a pessoa tem.
# Dependendo dessas respostas, ele sugere um passeio ou ficar em casa.

# Loop para obter uma resposta válida para o clima
while True:
    try:
        # Solicita ao usuário que informe o clima
        clima = int(input("Como está o clima? 1 - Sol ou 2 - Chuva: "))
        # Verifica se o valor digitado é válido (1 ou 2)
        if clima in [1, 2]:
            break
        else:
            print("Digite 1 para Sol ou 2 para Chuva.")
    except ValueError:
        # Trata o erro caso o usuário não digite um número
        print("❌ Entrada inválida. Digite um número inteiro (1 ou 2).")

# Loop para obter uma resposta válida para o valor de dinheiro
while True:
    try:
        dinheiro = int(input("Quanto de dinheiro você tem? "))
        break
    except ValueError:
        # Trata o erro caso o usuário não digite um número
        print("❌ Entrada inválida. Digite um valor numérico.")

# Verifica a condição para decidir o passeio com base no clima e no dinheiro disponível
if clima == 1 and dinheiro > 300:
    print("✅ Nós vamos no clube.")      # Clima de sol e dinheiro suficiente → vai ao clube
elif (clima == 2 or clima == 1) and dinheiro > 100:
    print("✅ Nós vamos no cinema.")    # Clima de chuva e dinheiro suficiente → vai ao cinema
else:
    print("✅ Nós vamos ficar em casa.") # Caso contrário → fica em casa