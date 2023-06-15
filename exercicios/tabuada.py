print(f'{" Exercício 009 ":=^40}')
num = int(input('Informe um número para a tabuada: '))
for c in range(1, 11):
    print(f'{num} X {c} = {c*num}')
print('Fim!!')

# Outra forma
cont = 1
while True:
    print(f'{num} X {cont} = {cont*num}')
    cont += 1 
    if cont == 11:
        break
print('Fim!!')
