curso = "Curso de Python"
palavra = "python"

# Pesquisa se a palavra existe dentro da string, ignorando maiúsculas/minúsculas
res = palavra.upper() in curso.upper()
print(res)

canal = "CFB Cursos"
res = curso + " do canal " + canal  # Concatena strings
print(res.upper())

cidade = "Rio de Janeiro"
dia = 9
mes = "Junho"
ano = 2025

# Concatenação de strings e conversão de inteiros para string
print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano))

# Utilizando o método format() para interpolação de strings
data = "{}, {} de {} de {}"
print(data.format(cidade, dia, mes, ano))

# Utilizando f-string (forma mais moderna e recomendada)
print(f"{cidade}, {dia} de {mes} de {ano}")
