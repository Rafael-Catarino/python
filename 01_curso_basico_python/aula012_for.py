# Programa que solicita 4 notas bimestrais e calcula a média

# Variável para armazenar a soma das notas
soma = 0

# Loop para solicitar as 4 notas ao usuário
for i in range(1, 5):
    nota = float(input(f"Informe a {i}ª nota: "))
    soma += nota

# Calcula a média dividindo a soma das notas por 4
media = soma / 4

# Exibe a média final formatada com 2 casas decimais
print(f"Média final: {media:.2f}")