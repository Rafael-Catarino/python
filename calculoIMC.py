'''Faça um programa que calcule o IMC da pessoa:'''

def getData(): 
  weight = float(input('Informe o seu peso em KG: '))
  height = float(input('Informe a sau altura em M: '))
  return calculatesBMI(weight, height)


def calculatesBMI(weight, height):
  bmi = weight / (height * height)
  return classifyingBMI(bmi)

def classifyingBMI(bmi):
  bmiv = f"{bmi:.2f}"
  if bmi < 18.5:
    return f'Você está a baixo do Peso. Seu peso é: {bmiv.replace(".",",")} KG.'
  elif bmi < 24.99:
    return f'Você está com peso Normal. Seu peso é: {bmiv.replace(".",",")} KG'
  elif bmi < 29.99:
    return f'Você está com Sobrepeso. Seu peso é: {bmiv.replace(".",",")} KG'
  elif bmi > 30:
    return f'Você está com Obesidade. Seu peso é: {bmiv.replace(".",",")} KG'


value = getData()
print(value)
