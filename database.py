import sqlite3
import peewee
from Entities.barrel import *

def iniciar_database():
    try:
        Usuarios.create_table()

        UsuariosCoins.create_table()

        Configuracao.create_table()

        Frases.create_table()

        LastestCleaning.create_table()

        print("Banco de dados está pronto.")
    except peewee.OperationalError:
        print("Não foi possível iniciar o banco!")