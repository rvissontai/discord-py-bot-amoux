import peewee
from Entities.base_model import BaseModel

class LastestCleaning(BaseModel):
    data = peewee.DateTimeField()