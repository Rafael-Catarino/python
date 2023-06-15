"""Faça um programa que calcule o IMC da pessoa:"""


def calculates_bmi(weight, height):
    bmi = weight / (height * height)
    return classifying_bmi(bmi)


def get_data():
    weight = float(input('Informe o seu peso em KG: '))
    height = float(input('Informe a sau altura em M: '))
    return calculates_bmi(weight, height)


def classifying_bmi(bmi):
    bmiv = f"{bmi:.2f}"
    if bmi < 18.5:
        return f'Você está a baixo do Peso. Seu peso é: {bmiv.replace(".",",")} KG.'
    elif bmi < 24.99:
        return f'Você está com peso Normal. Seu peso é: {bmiv.replace(".",",")} KG'
    elif bmi < 29.99:
        return f'Você está com Sobrepeso. Seu peso é: {bmiv.replace(".",",")} KG'
    elif bmi > 30:
        return f'Você está com Obesidade. Seu peso é: {bmiv.replace(".",",")} KG'


value = get_data()
print(value)
