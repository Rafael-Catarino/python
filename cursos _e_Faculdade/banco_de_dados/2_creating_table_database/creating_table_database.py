import sqlite3
from sqlite3 import Error
import os


#### - Codigo para se conectar ou banco de dados - ####
def creating_database_connection():
    directory = os.path.dirname(__file__)
    database_path = directory + "/cfbcurso_python.db"
    conection = None
    try:
        conection = sqlite3.connect(database_path)
    except Error as erro:
        print(erro)
    return conection


#### - Codigo para Criar Tabela - ####
connection = creating_database_connection()

database_code = """CREATE TABLE IF NOT EXISTS tb_contatos(
    N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
    T_NOMECONTATO VARCHAR(30),
    T_TELEFONECONTATO VARCHAR(30),
    T_EMAILCONTATO VARCHAR(30)
    ); """


"""def creating_table_database():
    try:
        c = create_database.cursor()
        c.execute(database_code)
    except Error as erro:
        print(erro)"""


#### Outra forma de criar uma tabela ###
def creating_table_database():
    with connection:
        connection.execute(database_code)


creating_table_database()
