import peewee
from Entities.base_model import BaseModel

class TaskInformeHumor(BaseModel):
    data = peewee.DateTimeField()