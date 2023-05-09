carro= {
    "Fabricante": "Honda",
    "Modelo": "HRV",
    "Ano": "2016",
    "Cor": "Prata"
}

print(carro["Fabricante"]) #Retorna o valor da chave Fabricante
print(carro.get("Ano")) #O .get retorna o valor da chave Ano

print("-----------------------")

carro["Cor"] = "Preto" #Muda o valor da chave Cor
print(carro)

print("-----------------------")

for x in carro:
    print(x) #Imprime as chaves do dictionary
    print(carro[x]) #Imprime o calor das chaves

print("-----------------------")

for c,v in carro.items():
    print(c + ": " + v) # Iprime o key e o value do dictionary

print("-----------------------")

carro["Cambio"]="Automatico" # Adiciona um novo elemento no dictionary
print(carro)

print("------------------------")

carro.pop("Cambio") #Também pode ser utilizado o del carro["Cambio"] - Removeo elemento no dictionary
print(carro)

print("-----------------------")

carro.clear() #Remove todo o dictinary 