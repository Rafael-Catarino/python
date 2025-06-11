curso = " Curso de Python "

print(curso)
print("Tamanho: " + str(len(curso)))

curso = curso.strip()  # Remove os espaços em branco do início e do final da string
print("----------------- Sem Espaço ---------------------")

print(curso)
print(curso[6])       # Imprime o caractere que está na posição 6
print(curso[0:5])     # Imprime os caracteres da posição 0 até 4 (5 não incluso)
print(curso[9:15])    # Imprime os caracteres da posição 9 até 14
print("Tamanho: " + str(len(curso)))  # Imprime o número de caracteres da string (sem os espaços laterais)
print(curso.lower())  # Converte toda a string para minúsculas
print(curso.upper())  # Converte toda a string para maiúsculas
print(curso.replace("Python", "C#"))  # Substitui "Python" por "C#"

arr = curso.split(" ")  # Divide a string em uma lista onde houver espaços
print(arr)              # Imprime a lista resultante
print(arr[2])           # Imprime o terceiro elemento da lista (posição 2)
