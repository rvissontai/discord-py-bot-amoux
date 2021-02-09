import discord
from discord.ext import commands

class bot_configuracoes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['atv'])
    async def atividade(self, ctx, *args):
        await bot.change_presence(activity=discord.Game(name="jogo da vida"))