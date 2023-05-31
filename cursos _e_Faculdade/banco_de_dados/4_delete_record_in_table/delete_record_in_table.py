import sqlite3
from sqlite3 import Error
import os


def create_connection_database():
    path_directory = os.path.dirname(__file__)
    database_path = path_directory+"/cfbcurso_python.db"
    try:
        connection = sqlite3.connect(database_path)
    except Error as erro:
        print(erro)
    return connection


def create_table():
    connection = create_connection_database()
    sql_code= "CREATE TABLE IF NOT EXISTS tb_contatos(N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT, T_NOMECONTATO VARCHAR(30), T_TELEFONECONTATO VARCHAR(30), T_EMAILCONATTO VARCHAR(30))"
    try:
        c=connection.cursor()
        c.execute(sql_code)
        connection.commit()
    except Error as erro:
        print(erro)

create_table()

def insert_data(name, tel, email):
    connction = create_connection_database()
    sql_code = "INSERT INTO tb_contatos(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONATTO)VALUES('"+name+"','"+tel+"','"+email+"');"
    try:
        c=connction.cursor()
        c.execute(sql_code)
        connction.commit()
    except Error as erro:
        print(erro)


def delete_data(num):
    connection = create_connection_database()
    sql_code = "DELETE FROM tb_contatos WHERE N_IDCONTATO='"+str(num)+"'"
    try:
        c=connection.cursor()
        c.execute(sql_code)
        connection.commit()
    except Error as erro:
        print(erro)

delete_data(8)