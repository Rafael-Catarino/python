""" Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. """
import os
os.system('clear')

def get_price():
    prices = []
    for i in range(1, 4):
        price = float(input(f'Informe o preço do {i}º produto: '))
        prices.append(price)
    get_cheapest_price(prices)

def get_cheapest_price(prices):
    price1 = prices[0]
    price2 = prices[1]
    price3 = prices[2]
    if (price1 <= price2) and (price1 <= price3):
        print(f'O preço mais barato é: {price1}')
    elif(price2 <= price1) and (price2 <= price3):
        print(f'O preço mais barato é: {price2}')
    elif(price3 <= price1) and (price3 <= price2):
        print(f'O preço mais barato é: {price3}')  

get_price()