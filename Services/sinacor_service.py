from Repository.SinacorRepository import *

class sinacor_service():
    def __init__(self, bot):
        self.repository = sinacor_repository()

    def verificar_status_sinacor(self):
        aberto = self.repository.verificar_status_sinacor()

        if aberto:
            return 'aberto'

        return 'fechado'

    def abrir(self):
        self.repository.abrir()

    def fechar(self):
        self.repository.fechar()
