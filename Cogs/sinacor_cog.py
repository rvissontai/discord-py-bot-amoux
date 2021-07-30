import discord

from discord.ext import commands
from Services.sinacor_service import *
from Util.parser_helper_util import CustomArgumentParser
from Parses.sinacor_parser import sinacor_parser

#TODO
#Utilizar o proprio argparse para gerar o conteúdo de ajuda que será enviado pelo bot
#Refatoração

class sinacor_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = sinacor_service(bot)
        self.sinacor_parser = sinacor_parser()
        self.comandos_internos = {
            '-a': self.abrir,
            '-f': self.fechar,
            '-s': self.verificar_status,
            '--fechar': self.fechar,
            '--abrir': self.abrir,
            '--status': self.verificar_status
        }

    @commands.command(pass_context=True)
    async def sinacor(self, ctx):
        parser = self.sinacor_parser.obter_parser()

        args = ctx.message.content.split(' ')[1:]

        mensagem = await ctx.send('Aguarde...')

        if len(args) == 0:
            
            await mensagem.edit(
                content = 'Você precisa informar um dos argumentos abaixo.',
                embed = discord.Embed(title="Ajuda", description=''.join(self.sinacor_parser.obter_ajuda())))
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