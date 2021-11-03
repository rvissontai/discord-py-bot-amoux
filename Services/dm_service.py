import json

from Util.parser_helper_util import CustomArgumentParser
from Services.cadmus_coins_service import cadmus_coins_service
from Entities.usuarios_coins_model import UsuariosCoins


class dm_service():
    def __init__(self, bot):
        self.bot = bot
        self.servicos_disponiveis = ['coin']
        self.coin_service = cadmus_coins_service(bot)

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

            await self.coin_teste_autenticacao(message, parse_args_result)
        except SystemExit as e:
            await message.channel.send("Ocorreu um erro ao validar o comando.")


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