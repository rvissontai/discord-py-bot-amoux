import discord
from Util.parser_helper_util import CustomArgumentParser, string_para_args_parse
from Services.cadmus_coins_service import cadmus_coins_service
from Services.goobee_teams_service import goobe_teams_service
from Entities.usuarios_coins_model import UsuariosCoins
from Entities.usuarios_model import Usuarios
import json

class dm_service():
    def __init__(self, bot):
        self.bot = bot
        self.servicos_disponiveis = ['coin', 'goobe']
        self.coin_service = cadmus_coins_service(bot)
        self.goobe_service = goobe_teams_service(bot)

    async def handle_private_message(self, message):
        parser = CustomArgumentParser(description='Registrar acesso.')

        parser.add_argument('-s', '--service', help='Service', required=True)
        parser.add_argument('-l', '--login', help='Login', required=True)
        parser.add_argument('-p', '--password', help='Password', required=True)

        try:
            args = message.content.split(' ')

            parse_args_result = parser.parse_args(args)

            if parser.error_message:
                await message.channel.send(parser.error_message)
                return
                        
            if parse_args_result.service not in self.servicos_disponiveis:
                await message.channel.send("Somente são permitidos os serguintes services: " + str(self.servicos_disponiveis))
                return        

            await self.goobe_teste_autenticacao(message, parse_args_result)
        except SystemExit as e:
            await message.channel.send("Ocorreu um erro ao validar o comando.")


    async def goobe_teste_autenticacao(self, message, args):
        try:
            #Utilizar um sistema...humm...alternatvo... sim, alternativo, para encontrar a info criptografada
            await message.channel.send("1 de 3 - Encriptografando credencias, essa é a parte mais demorada, espera aí...")
            encripted = await self.goobe_service.encriptar_autenticacao(args.login, args.password)

            await message.channel.send("2 de 3 - Autenticando no goobe...")
            response = await self.goobe_service.autenticar(encripted["login"], encripted["password"])

            if(response.status_code == 200):
                try:
                    user = Usuarios.get(Usuarios.idDiscord == message.author.id)
                    await message.channel.send("3 de 3 - Atualizando usuário...")
                    Usuarios.update(login = encripted["login"], senha = encripted["password"]).where(Usuarios.idDiscord == message.author.id).returning(Usuarios)
                except Usuarios.DoesNotExist:
                    await message.channel.send("3 de 3 - Criando usuário...")
                    Usuarios.insert(idDiscord=message.author.id, login=encripted["login"], senha=encripted["password"]).execute()
                
                await message.channel.send('Beleza, consegui logar aqui, agora é só ir no chat geral e mudar seu humor.')
            else:
                await message.channel.send('Não foi possível autenticar, tem certeza que me passou as informações certas?')
        except:
            await message.channel.send('Vixi ocorreu um problema interno, não vai rolar ):')

    async def coin_teste_autenticacao(self, message, args):
        response = await self.coin_service.autenticar(args.login, args.password)

        if(response.status_code != 200):
            await message.channel.send('Cara alguma coisa deu errada, eu não consegui fazer a requisição ):')
            return

        content = json.loads(response.text)

        if content['IsThereLoginError']:
            await message.channel.send('Não foi possível autenticar, tem certeza que me passou as informações certas?')
            return

        try:
            user = UsuariosCoins.get(UsuariosCoins.idDiscord == message.author.id)
            UsuariosCoins.update(login = args.login, senha = args.password).where(UsuariosCoins.idDiscord == message.author.id).execute()
        except UsuariosCoins.DoesNotExist:
            UsuariosCoins.insert(idDiscord=message.author.id, login=args.login, senha=args.password).execute()

        await message.channel.send('Beleza, consegui logar aqui, ta liberado pra fazer pix!')