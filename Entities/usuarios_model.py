import peewee
from Entities.base_model import BaseModel

class Usuarios(BaseModel):
    idDiscord = peewee.TextField(unique=True)
    login = peewee.TextField()
    senha = peewee.TextField()