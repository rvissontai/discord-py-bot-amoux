import datetime

from database import HumorDiario

class humor_diario_repository:

    def adicionar(self, idDiscord):
        hoje = datetime.date.today()
        humor = self.obter(idDiscord, hoje)

        if humor is not None:
            HumorDiario.update(data = hoje).where(HumorDiario.idDiscord == idDiscord, HumorDiario.data == hoje).returning(HumorDiario)

        HumorDiario.insert(idDiscord=idDiscord, data=hoje).execute()


    def obter(self, idDiscord, data):
        try:
            return HumorDiario.get(
                HumorDiario.idDiscord == idDiscord,
                HumorDiario.data == data
            )
        except HumorDiario.DoesNotExist:
            return None
