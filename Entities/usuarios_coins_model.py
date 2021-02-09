import peewee
from Entities.base_model import BaseModel

class UsuariosCoins(BaseModel):
    idDiscord = peewee.TextField(unique=True)
    login = peewee.TextField()
    senha = peewee.TextField()