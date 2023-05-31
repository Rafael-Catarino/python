import sqlite3
from sqlite3 import Error
import os


#### - Criar conexão com o banco de dados ####
def create_database_conection():
    directory_path = os.path.dirname(__file__)
    database_path = directory_path + "/cfbcurso_python.db"
    try:
        connection = sqlite3.connect(database_path)
    except Error as erro:
        print(erro)
    return connection


#### - Criar tabela - ####
connection = create_database_conection()

database_code = """CREATE TABLE IF NOT EXISTS tb_contatos(
    N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
    T_NOMECONTATO VARCHAR(30),
    T_TELEFONECONTATO VARCHAR(30),
    T_EMAILCONTATO VARCHAR(30)
    );"""


"""def creating_table_database():
    try:
        c = connection.cursor()
        c.execute(database_code)
    except Error as erro:
        print(erro)
"""


#### - Outra forma de criar tabela - ####
def creating_table_database():
    with connection:
        connection.execute(database_code)


creating_table_database()


#### inserindo dado na tabela ####
def inserting_record_into_table(name, telphone, email):
    with connection:
        connection.execute(
            """INSERT INTO tb_contatos(
                T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)
                VALUES(?, ?, ?);""",(name, telphone, email)
        )