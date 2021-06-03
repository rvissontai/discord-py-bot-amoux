import requests
import os
from Entities.usuarios_coins_model import UsuariosCoins
import json
class cadmus_coins_service():
    def __init__(self, bot):
        self.bot = bot
        self.url_auth = os.getenv('CADMUS-COINS-URL') + os.getenv('CADMUS-COINS-ENDPOINT-AUTH')
        self.url_transfer = os.getenv('CADMUS-COINS-URL') + os.getenv('CADMUS-COINS-ENDPOINT-TRANSFER')

    async def autenticar(self, email, senha):
        return requests.post(self.url_auth, data=None, json={'Email': email, 'Password': senha, 'IsThereLoginError': False })

    async def transferir(self, ctx):
        try:
            user = UsuariosCoins.get(UsuariosCoins.idDiscord == ctx.author.id)
            response = await self.autenticar(user.login, user.senha)

            if(response.status_code == 200):
                request_transfer = { 'To': 1294, 'From': 1299, 'Amount': 1, 'Message': 'teste 2' }

                content = json.loads(response.content)

                header = { 'Authorization': 'Bearer ' + content["Info"]["TokenApi"] }
                response_transfer = requests.post(self.url_transfer, json=request_transfer, headers=header)

                if response_transfer:
                    await ctx.author.send('Transferencia concluída com sucesso.')     

        except UsuariosCoins.DoesNotExist:
            await ctx.author.send('Agora é só me falar seu email e senha em uma única mensagem beleza? é só separar por espaço... fica tranquilo que não sou X9.')     
    