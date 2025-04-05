import os
restaurantes = [{"nome": "Craque do Pão", "categoria": "Padaria", "ativo": False},
                {"nome": "Come Quieto", "categoria": "Comida", "ativo": True},
                {"nome": "Som Sushi", "categoria": "Japones", "ativo": True}]


def exibir_nome_do_programa():
    print("🆂🅰🅱🅾🆁 🅴🆇🅿🆁🅴🆂🆂\n")


def exibir_subtitulo(titulo):
    os.system("cls")
    linha = "*" * (len(titulo))
    print(linha)
    print(titulo)
    print(linha)


def voltar_ao_menu_principal():
    input("\nDigite uma letrar para voltar ao menu inicial: ")
    main()


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome = input("Digite o nome do restaurante que você deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {nome}: ")
    restaurante = {"nome": nome, "categoria": categoria, "ativo": False}
    restaurantes.append(restaurante)
    print(f"\nO restaurante {nome} foi cadastrado com sucesso.")
    voltar_ao_menu_principal()


def lista_de_restaurante():
    exibir_subtitulo("Listando os restaurantes")
    print(f"{"Nome do Restaurante".ljust(23)} | {"Categoria".ljust(20)} | Status")
    print("-"*60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(
            f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
    voltar_ao_menu_principal()


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Lista restaurante")
    print("3. Alternae estado do restaurante")
    print("4. Sair")


def option_invalida():
    print("Opção invalida!")
    voltar_ao_menu_principal()


def alterna_estado_restaurante():
    exibir_subtitulo("Alternado estado do restaurante")
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado:')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_do_restaurante} foi ativado com sucesso" if restaurante[
                "ativo"] else f"O restaurante {nome_do_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print(f"O restaurante {nome_do_restaurante} não foi encontrado")
    voltar_ao_menu_principal()


def esclhe_opcao():
    try:
        option_chosen = int(input("Escolha uma opçâo: "))
        if option_chosen == 1:
            cadastrar_novo_restaurante()
        elif option_chosen == 2:
            lista_de_restaurante()
        elif option_chosen == 3:
            alterna_estado_restaurante()
        elif option_chosen == 4:
            finalizar_app()
        else:
            option_invalida()
    except:
        option_invalida()


def finalizar_app():
    exibir_subtitulo("Finalizando o Sistema")


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    esclhe_opcao()


if __name__ == "__main__":
    main()
