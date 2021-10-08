import discord

from discord.ext import commands, tasks
from Services.central_risco_service import central_risco_service
from Parses.central_risco_parser import central_risco_parser
from Util.parser_helper_util import string_para_args_parse

class central_risco_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = central_risco_service()
        self.parser = central_risco_parser()
        self.comandos_internos = {
            '-a': self.aprovar_ordem,
            '--aprovar_ordem': self.aprovar_ordem
        }
        

    @commands.command(pass_context=True, aliases=['cr'])
    async def central(self, ctx):
        mensagem = await ctx.send('Aguarde...')

        try:
            args = ctx.message.content.split(' ')[1:]

            parser = self.parser.obter_parser()

            parse_args_result = parser.parse_args(args)

            if parser.error_message:
                await mensagem.edit(content = parser.error_message)
                return

            self.comandos_internos[args[0]](args[1])

            await mensagem.edit(content = "Ordem enviada para o rabbit na central de risco.")
        except Exception as e:
            await mensagem.edit(content = "Ocorreu um erro ao validar o comando.")

        

    def aprovar_ordem(self, ordem):
        self.service.aprovar_ordem(ordem)

def setup(bot):
    bot.add_cog(central_risco_cog(bot))