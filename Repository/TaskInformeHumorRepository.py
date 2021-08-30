import datetime

from database import TaskInformeHumor

class task_informe_humor_repository:

    def adicionar(self):
        hoje = datetime.date.today()
        task = self.obter_por_data(hoje)

        if task is not None:
            task.data = hoje
            task.save()
        else:
            TaskInformeHumor.insert(data=hoje).execute()


    def obter_por_data(self, data):
        try:
            return TaskInformeHumor.get(TaskInformeHumor.data == data)
            
        except TaskInformeHumor.DoesNotExist:
            return None

    def obter(self):
        try:
            return TaskInformeHumor.get(TaskInformeHumor.data == datetime.date.today())
            
        except TaskInformeHumor.DoesNotExist:
            return None