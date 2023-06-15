import sqlite3


# - Criar banco de dados - #
def create_database():
    connection = sqlite3.connect("""C:\\vscode\\estacio\\python\\banco_de_dados\\database""")
    return connection


# - Criar tabela - #
def creating_table_database():
    connection = create_database()
    with connection:
        connection.execute("""CREATE TABLE IF NOT EXISTS tb_contatos(
    N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
    T_NOMECONTATO VARCHAR(30),
    T_TELEFONECONTATO VARCHAR(30),
    T_EMAILCONTATO VARCHAR(30)
    );""")


# - Inserir um registro na tabela - #
def inserting_data(name, telphone, email):
    connection = create_database()
    with connection:
        connection.execute("""INSERT INTO tb_contatos(T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)
                VALUES(?, ?, ?);""", (name, telphone, email))


def delete_data():
    connection = create_database()
    with connection:
        connection.execute("""DELETE FROM tb_contatos WHERE id = ?;""", (id,))


def update_data():
    connection = create_database()
    with connection:
        connection.execute("UPDATE tb_contatos SET T_NOMECONTATO='FAFA' WHERE N_IDCONTATO='2'")
