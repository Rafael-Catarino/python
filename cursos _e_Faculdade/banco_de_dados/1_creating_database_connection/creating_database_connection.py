import sqlite3
from sqlite3 import Error
import os


def create_database():
    directory_path = os.path.dirname(__file__)
    database_path = directory_path + "/cfbcurso_python.db"
    try:
        conection = sqlite3.connect(database_path)
    except Error as erro:
        print(erro)
    return conection


### - Outra forma de fazer - ####
"""def create_database():
    conection = sqlite3.connect("D:\\vscode\\estudos\\estacio\\python\\cursos _e_Faculdade\\banco_de_dados\\1_creating_database_connection") 
    return conection"""

create_database()