'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

def generating_coupon():
    request = {}
    print('--------------------')
    get_type_of_meat(request)
    print('--------------------')
    get_form_of_payment(request)
    print('--------------------')
    get_kg(request)
    calc_price(request)
    return request

def calc_price(request):
    if request['Carne'] == 'File Duplo':
        if request['forma de pagamento'] == 'cartão tabajara':
            if float(request['quilograma(s)']) > 5:
                discount = (request['quilograma(s)'] * 5.8)* 0.05
                total_price = request['quilograma(s)'] * 5.8
                request['valor pagamento'] = total_price - discount
            elif request['quilograma(s)'] < 5:
                discount = (request['quilograma(s)'] * 4.9)* 0.05
                total_price = request['quilograma(s)'] * 4.9
                request['valor pagamento'] = total_price - discount
        elif request['forma de pagamento'] == 'dinheiro':
            if request['quilograma(s)'] > 5:
                total_price = request['quilograma(s)'] * 5.8
                request['valor pagamento'] = total_price
            if request['quilograma(s)'] < 5:
                discount = (request['quilograma(s)'] * 4.9)* 0.05
                total_price = request['quilograma(s)'] * 4.9
                request['valor pagamento'] = total_price - discount

    elif request['carne'] == 'Alcatra':
        if request['forma de pagamento'] == 'cartão tabajara':
            if request['quilograma'] > 5:
                
            if request['quilograma'] < 5:
        elif request['forma de pagamento'] == 'dinheiro':
    else:
        if request['forma de pagamento'] == 'cartão tabajara':

        elif request['forma de pagamento'] == 'dinheiro':

def get_kg(request):
    kg = float(input('Informe a quantidade de carne em KG: '))
    request['quilograma(s)'] = kg

def get_form_of_payment(request):
    print('Qual a forma de pagamento?')
    form_of_payment = int(input('Digite 1- cartão tabajara e 2- dinheiro: '))
    while(form_of_payment):
        if form_of_payment == 1:
            request['forma de pagamento'] = 'cartão tabajara'
            break
        elif form_of_payment == 2:
            request['forma de pagamento'] = 'dinheiro'
            break
        else:
            print('--------------------')
            print('Você informou um número invalido:')
            print('Qual a forma de pagamento?')
            form_of_payment = int(input('Favor digitar 1- cartão tabajara e 2- dinheiro: '))

def get_type_of_meat(request):
    print('Qual carne você deseja escolher?')
    type_of_meat = int(input('Digite 1- File Duplo, 2- Alcatra e 3-Picanha: '))
    while(type_of_meat):
        if type_of_meat == 1:
            request['Carne'] = 'File Duplo'
            break
        elif type_of_meat == 2:
            request['Carne'] = 'Alcatra'
            break
        elif type_of_meat == 3:
            request['Carne'] = 'Picanha'
            break
        else:
            print('--------------------')
            print('Você informou um número invalido:')
            print('Qual carne você deseja escolher?')
            type_of_meat = int(input('Favor digitar 1- File Duplo, 2- Alcatra e 3-Picanha: '))

coupon = generating_coupon()
print(coupon)