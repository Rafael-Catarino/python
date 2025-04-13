# para criar um ambiente virtual com python basta usar os seguintes codigos no teminal
# para criar um novo ambiente virtual: python -m venv venv
# ativar o ambiente virtual: no windows - nome_do_ambiente\Scripts\activate
#                            no linux - source nome_do_ambiente\Scripts\activate
#                            no bash - source nome_do_ambiente/bin/activate
# para desativar o ambiente: deactivate
# criar um arquivo requirements.txt para listar as dependencias do projeto: pip freeze > requirements.txt
# instalar os dependencias  para ser usado no projeto: pip install nome da dependencia.

import requests # importa a biblioteca request.


url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item["Company"]
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item["Item"],
            "price": item["price"],
            "descricao": item["description"]
        })
else:
    print(f"O erro foi {response.status_code}")


print(dados_restaurante["KFC"])
