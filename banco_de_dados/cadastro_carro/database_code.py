import sqlite3
from sqlite3 import Error
import os


# - Cria o banco de dados - #
def create_connection_database():
    path_directory = os.path.dirname(__file__)
    database_path = path_directory + "/database.db"
    connection = None
    try:
        connection = sqlite3.connect(database_path)
    except Error as erro:
        print(erro)
    return connection


# - Cria tabela no banco de dados - #
def create_table():
    connection = create_connection_database()
    sql_code = "CREATE TABLE IF NOT EXISTS tb_carro(i_id INTEGER PRIMARY KEY AUTOINCREMENT," \
               " v_nome VARCHAR(30), v_marca VARCHAR(30), v_cor VARCHAR(30))"
    try:
        c = connection.cursor()
        c.execute(sql_code)
        connection.commit()
    except Error as erro:
        print(erro)


create_table()


# - Insere um registro no banco - #
def insert_data(nome, marca, cor):
    connction = create_connection_database()
    sql_code = (
        "INSERT INTO tb_carro(v_nome, v_marca, v_cor)"
        "VALUES('" + nome + "','" + marca + "','" + cor + "');"
    )
    try:
        c = connction.cursor()
        c.execute(sql_code)
        connction.commit()
    except Error as erro:
        print(erro)


# - Deleta um registro do banco - #
def delete_data(num):
    connection = create_connection_database()
    sql_code = "DELETE FROM tb_carro WHERE i_id='" + str(num) + "'"
    try:
        c = connection.cursor()
        c.execute(sql_code)
        connection.commit()
    except Error as erro:
        print(erro)


# - Altera um registro - #
def update_data(name, brand, color, id_car):
    connection = create_connection_database()
    sql_code = "UPDATE tb_carro SET v_nome='" + name + "', v_marca='" + brand + "', v_cor='" + color + \
               "' WHERE i_id='" + id_car + "'"
    try:
        c = connection.cursor()
        c.execute(sql_code)
        connection.commit()
    except Error as erro:
        print(erro)


# - Pega todos os registros do banco de dados - #
def select_car():
    connection = create_connection_database()
    sql_code = "SELECT * FROM tb_carro"
    c = connection.cursor()
    c.execute(sql_code)
    result = c.fetchall()
    return result
