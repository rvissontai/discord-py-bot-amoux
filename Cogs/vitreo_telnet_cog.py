import discord
from discord.ext import commands
from Services.vitreo_telnet_service import vitreo_telnet_service

class vitreo_telnet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = vitreo_telnet_service(self.bot)

    # @commands.command(pass_context=True, aliases=['limpar-cache', 'lc', 'LC'])
    # async def limpar_cache(self, ctx):
    #     mensagem = await ctx.send('limpando...')
    #     sucesso = await self.service.limpar_cache()

    #     if (sucesso):
    #         await mensagem.edit(content = 'Cache homol foi limpo com sucesso!')
    #     else:
    #         await mensagem.edit(content = 'Não consegui limpar o cache, alguma coisa deu errado ):')

def setup(bot):
    bot.add_cog(vitreo_telnet(bot))