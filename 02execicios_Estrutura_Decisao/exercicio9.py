"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

arrNum = []
arrNumOrder = []

for k in range(1, 4):
    arrNum.append(int(input(f"Informe o {k}º numero: ")))

if arrNum[0] > arrNum[1] and arrNum[0] > arrNum[2]:
    arrNumOrder.append(arrNum[0])

    if arrNum[1] > arrNum[2]:
        arrNumOrder.append(arrNum[1])
        arrNumOrder.append(arrNum[2])
    else:
        arrNumOrder.append(arrNum[2])
        arrNumOrder.append(arrNum[1])

elif arrNum[1] > arrNum[2] and arrNum[1] > arrNum[0]:
    arrNumOrder.append(arrNum[1])

    if arrNum[0] > arrNum[2]:
        arrNumOrder.append(arrNum[0])
        arrNumOrder.append(arrNum[2])
    else:
        arrNumOrder.append(arrNum[2])
        arrNumOrder.append(arrNum[0])

else:
    arrNumOrder.append(arrNum[2])

    if arrNum[0] > arrNum[1]:
        arrNumOrder.append(arrNum[0])
        arrNumOrder.append(arrNum[1])
    else:
        arrNumOrder.append(arrNum[1])
        arrNumOrder.append(arrNum[0])

print(arrNumOrder)
