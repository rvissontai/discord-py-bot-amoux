import cx_Oracle
import os

def criar_conexao_oracle():
    return cx_Oracle.connect(os.getenv('ORACLE_CONNECTION_STRING'))