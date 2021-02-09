import discord
from discord.ext import commands
from parses import coins_parser
from Services.cadmus_coins_service import cadmus_coins_service

class cadmus_coins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = cadmus_coins_service(bot)

    @commands.command(pass_context=True, aliases=['transfer-coins'])
    async def coins(self, ctx, *args):
        print(coins_parser.parse_args(args))

def setup(bot):
    bot.add_cog(cadmus_coins(bot))