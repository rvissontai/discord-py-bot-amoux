from Repository.OracleConnection import *

class sinacor_repository:
    def verificar_status_sinacor(self):
        conexao = criar_conexao_oracle()

        cursor = conexao.cursor()

        query = """
            SELECT 
                TP_MOVIMENTO
            FROM 
                TCCPARAM
            WHERE
                (TP_MOVIMENTO = 'AB')
                AND (to_char(DT_ATUAL ,'yyyy-MM-dd') = to_char(SYSDATE ,'yyyy-MM-dd'))
                AND (rownum = 1) 
            ORDER BY DT_ATUAL DESC"""

        cursor.execute(query)

        aberto = False

        if cursor is None:
            aberto = False

        for row in cursor:
            aberto = True

        conexao.close()

        return aberto


    def fechar(self):
        self.__mudar_status('FE')


    def abrir(self):
        self.__mudar_status('AB')


    def __mudar_status(self, status):
        conexao = criar_conexao_oracle()

        cursor = conexao.cursor()

        query = f"UPDATE CORRWIN.TCCPARAM SET TP_MOVIMENTO = '{status}' WHERE (rownum = 1)"

        cursor.execute(query)

        conexao.commit()

        conexao.close()

        return
