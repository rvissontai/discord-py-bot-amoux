import discord
import argparse
import shlex
import os
import requests

from discord.ext import commands
from Services.cadmus_coins_service import cadmus_coins_service
from Util.parser_helper_util import CustomArgumentParser, string_para_args_parse
from database import UsuariosCoins
from Services.goobee_teams_service import goobe_teams_service

class cadmus_coins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = cadmus_coins_service(bot)

    @commands.command(pass_context=True, aliases=['pix'])
    async def coins(self, ctx, *args):
        await self.service.transferir(ctx)
        
        parser = CustomArgumentParser(description='Transferir coins.')
        parser.add_argument('-l', '--login', help='Login', required=True)
        parser.add_argument('-s', '--senha', help='Senha', required=True)

        try:
            param = string_para_args_parse(*args)
            parse_args_result = parser.parse_args(param)

            if parser.error_message:
                await ctx.send(parser.error_message)
            #print(parse_args_result)
        except SystemExit as e:
            await ctx.send("Ocorreu um erro ao validar o comando pix.")

    async def autenticar(self, user, senha):
        return requests.post(self.url_auth, data=None, json={'Email': user, 'Password': senha, 'IsThereLoginError': False, 'ErrorMessage': '' })

def setup(bot):
    bot.add_cog(cadmus_coins(bot))

