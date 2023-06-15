"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""
import os
os.system('clear')

c = int(input('Informe a temperatura em graus Celcius: '))
print(c)
f = (c * 1.8) + 32
print(f'{c}º celcius equivale a {f}º fahrenheit')
