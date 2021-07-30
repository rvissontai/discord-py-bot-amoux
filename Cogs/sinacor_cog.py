import discord

from discord.ext import commands
from Services.sinacor_service import *
from Util.parser_helper_util import CustomArgumentParser

#TODO
#Utilizar o proprio argparse para gerar o conteúdo de ajuda que será enviado pelo bot
#Refatoração

class sinacor_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = sinacor_service(bot)
        self.comandos_internos = {
            '-a': self.abrir,
            '-f': self.fechar,
            '-s': self.verificar_status,
            '--fechar': self.fechar,
            '--abrir': self.abrir,
            '--status': self.verificar_status
        }

    @commands.command(pass_context=True, aliases=['sinacor'])
    async def status_sinacor(self, ctx):
        parser = CustomArgumentParser(description='Sinacor')

        parser.add_argument('-s', '--status', help='Verificar se o sinacor está aberto ou fechado', action='store_true')
        parser.add_argument('-a', '--abrir', help='Abrir o sinacor', action='store_true')
        parser.add_argument('-f', '--fechar', help='Fechar o sinacor', action='store_true')

        args = ctx.message.content.split(' ')[1:]

        ajuda = [
            '\t-s --status \t Verificar se o sinacor está aberto ou fechado.\n', 
            '\t-a --abrir  \t Abrir o sinacor\n', 
            '\t-f --fechar \t Fechar o sinacor'
        ]

        mensagem = await ctx.send('Aguarde...')

        if len(args) == 0:
            
            await mensagem.edit(
                content = 'Você precisa informar um dos argumentos abaixo.',
                embed = discord.Embed(title="Ajuda", description=''.join(ajuda)))
            return

        parse_args_result = parser.parse_args(args)

        if parser.error_message:
            await mensagem.edit(content = parser.error_message)
            return

        await self.comandos_internos[args[0]](mensagem)

        
    @commands.command(pass_context=True, aliases=['ss'])
    async def ver_status_sinacor(self, ctx):
        mensagem = await ctx.send('Aguarde...')
        await self.verificar_status(mensagem)


    @commands.command(pass_context=True, aliases=['sa'])
    async def abrir_sinacor(self, ctx):
        mensagem = await ctx.send('Aguarde...')
        await self.abrir(mensagem)


    @commands.command(pass_context=True, aliases=['sf'])
    async def fechar_sinacor(self, ctx):
        mensagem = await ctx.send('Aguarde...')
        await self.fechar(mensagem)

    async def verificar_status(self, mensagem):
        try:
            response = self.service.verificar_status_sinacor()
            await mensagem.edit(content = f'Sinacor está `{response}`')
        except Exception as e:
            await mensagem.edit(content = 'Erro ao verificar status.')
            print(e)


    async def abrir(self, mensagem):
        try:
            self.service.abrir()
            await mensagem.edit(content = f'Status do Sinacor modificado para `aberto`.')
        except Exception as e:
            await mensagem.edit(content = 'Erro ao abrir Sinacor.')
            print(e)


    async def fechar(self, mensagem):
        try:
            self.service.fechar()
            await mensagem.edit(content = f'Status do Sinacor modificado para `fechado`.')
        except Exception as e:
            await mensagem.edit(content = 'Erro ao abrir Sinacor.')
            print(e)

def setup(bot):
    bot.add_cog(sinacor_cog(bot))