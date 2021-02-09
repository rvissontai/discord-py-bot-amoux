import peewee
from Entities.base_model import BaseModel

class Frases(BaseModel):
    id = peewee.AutoField()
    Autor = peewee.TextField(),
    Texto = peewee.TextField()