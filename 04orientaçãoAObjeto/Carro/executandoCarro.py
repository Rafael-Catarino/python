from Carro import Carro

carro1 = Carro('9ASWX000001',2,1.8,0)

print('Chassi: ',carro1.chassi)
print('Cor: ', ('Azul' if carro1.cor==1 else 'Branco'))
print ("Motor: ", carro1.motor)

if (carro1.tem_Gasolina() == False):
    print('Precisa abastecer')
else:
    carro1.ligar()
