import requests
import os

class cadmus_coins_service():
    def __init__(self, bot):
        self.bot = bot
        self.url_auth = os.getenv('CADMUS-COINS-URL') + os.getenv('CADMUS-COINS-ENDPOINT-AUTH')

    async def autenticar(self, email, senha):
        return requests.post(self.url_auth, data=None, json={'Email': email, 'Password': senha, 'IsThereLoginError': False })

    