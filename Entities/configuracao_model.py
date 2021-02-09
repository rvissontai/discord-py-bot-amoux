import peewee
from Entities.base_model import BaseModel

class Configuracao(BaseModel):
    chave = peewee.TextField(unique=True)
    valor = peewee.TextField()