import requests
import json
from database import Usuarios
from datetime import timezone, datetime
import os

class goobe_teams_service():
    def __init__(self, bot):
        self.bot = bot
        self.url_auth = os.getenv('GOOBEE-URL') + os.getenv('GOOBE-ENDPOINT-AUTH')
        self.url_humor = os.getenv('GOOBEE-URL') + os.getenv('GOOBE-ENDPOINT-HUMOR')
        self.url_daily = os.getenv('GOOBEE-URL') + os.getenv('GOOBEE-ENDPOINT-DAILY')

    async def autenticar(self, user, senha):
        return requests.post(self.url_auth, data=None, json={'Usuario': user, 'Senha': senha })

    async def add_humor(self, ctx, id_sentimento):
        mensagem = await ctx.send('Definindo humor...')
        
        try:
            user = Usuarios.get(Usuarios.idDiscord == ctx.author.id)
            response = await self.autenticar(user.login, user.senha)
            
            if(response.status_code == 200):
                sucesso_response = json.loads(response.text)

                header = { 'Authorization': 'Bearer ' + sucesso_response["token"] }
                param = {
                    'idPessoa': sucesso_response["idPessoa"],
                    'idResponsavelCriacao': sucesso_response["id"],
                    'sentimento': id_sentimento
                }

                humorResponse = requests.post(self.url_humor, json=param, headers=header)

                if(humorResponse.status_code == 200):
                    await mensagem.edit(content = 'Seu humor foi alterado!')
                else :
                    await mensagem.edit(content = 'Cara alguma coisa errada não ta certa, não consegui alterar o humor ):')
            else:
                await mensagem.edit(content = 'Cara deu alguma coisa errada com sua autenticação ):')

        except Usuarios.DoesNotExist:
            await ctx.author.send('Agora é só me falar seu email e senha em uma única mensagem beleza? é só separar por espaço... fica tranquilo que não sou X9.')     

    async def realizar_daily(self, ctx) :
        mensagem = await ctx.send('Definindo daily...')

        try:
            user = Usuarios.get(Usuarios.idDiscord == ctx.author.id)
            response = await self.autenticar(user.login, user.senha)
            
            if(response.status_code == 200):
                sucesso_response = json.loads(response.text)

                header = { 'Authorization': 'Bearer ' + sucesso_response["token"] }
                param = {
                    'dia': datetime.now().isoformat(),
                    'idResponsavelRegistro': sucesso_response["idPessoa"],
                    'idTime': 'fce0b9b1-f697-4baf-9641-1480f495ee4a'
                }

                response = requests.post(self.url_daily, json=param, headers=header)

                if(response.status_code == 200):
                    await mensagem.edit(content = 'Daily definida como realizada!')
                else :
                    await mensagem.edit(content = 'Cara alguma coisa errada não ta certa, não consegui realizar a daily. ):')

            else:
                await ctx.author.send('Cara deu alguma coisa errada com sua autenticação ):')                

        except Usuarios.DoesNotExist:
            await ctx.author.send('Agora é só me falar seu email e senha em uma única mensagem beleza? é só separar por espaço... fica tranquilo que não sou X9.')     
        except Exception as e:
            await mensagem.edit(content = 'Cara alguma coisa errada não ta certa, não consegui realizar a daily ):')
            print(e)