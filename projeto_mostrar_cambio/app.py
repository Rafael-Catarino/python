import requests

url ="https://economia.awesomeapi.com.br/last/USD-BRL"


def pega_valor_em_reais():
  valor_em_real = int(input("Informe o valor que você quer em Reais:"))
  pega_valor_de_cambio(valor_em_real)


def pega_valor_de_cambio(valor_em_real):
  response = requests.get(url)
  if response.status_code == 200:
    dados_json = response.json()
    valor_da_compra_em_dolar = float(dados_json["USDBRL"]["bid"]) * valor_em_real
    valor_da_venda_em_dolar = float(dados_json["USDBRL"]["ask"]) * valor_em_real
    mostra_resultado(valor_da_venda_em_dolar, valor_da_compra_em_dolar, valor_em_real)
  else:
    print(f"O erro foi {response.status_code}")


def mostra_resultado(valor_da_venda_em_dolar, valor_da_compra_em_dolar, valor_em_real):
  print(f"Compra - US: {valor_em_real} = R$ {valor_da_compra_em_dolar}\n")
  print(f"Venda - US: {valor_em_real} = R$ {valor_da_venda_em_dolar}\n")

pega_valor_em_reais()