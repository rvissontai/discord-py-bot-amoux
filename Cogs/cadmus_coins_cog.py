import discord
import argparse
import shlex

from discord.ext import commands
from parses import coins_parser
from Services.cadmus_coins_service import cadmus_coins_service
from Util.parser_helper_util import string_para_args_parse

class cadmus_coins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = cadmus_coins_service(bot)

    @commands.command(pass_context=True, aliases=['transfer-coins'])
    async def coins(self, ctx, *args):
        parser = argparse.ArgumentParser(description='Transferir coins.')
        parser.add_argument('-l', '--login', help='Login', required=True)
        parser.add_argument('-s', '--senha', help='Senha', required=True)

        try:
            param = string_para_args_parse(*args)
            parse_args_result = parser.parse_args(param)
            #print(parse_args_result)
        except SystemExit as e:
            await ctx.send(parse_args_result)

def setup(bot):
    bot.add_cog(cadmus_coins(bot))