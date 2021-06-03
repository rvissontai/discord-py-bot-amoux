import discord 
import requests
import json
import argparse
import os

from discord.ext import commands
from database import iniciar_database
from settings import *

from Services.goobee_teams_service import goobe_teams_service
from database import Usuarios

from Cogs.barrel import *
from Services.dm_service import dm_service

bot = commands.Bot(command_prefix = ["?", "."])

iniciar_database()

@bot.event
async def on_ready():
    bot.load_extension("Cogs.goobee_teams_cog")
    bot.load_extension("Cogs.vitreo_telnet_cog")
    bot.load_extension("Cogs.cadmus_coins_cog")

    print('Bot está pronto')

    await bot.change_presence(activity=discord.Game(name="jogo da vida"))
    
@bot.event
async def on_message(message):
    print(str(message.author) + ' enviou uma mensagem')

    if message.author.bot:
        return

    private_message = message.author.dm_channel is not None and message.channel.id == message.author.dm_channel.id

    if private_message: 
        # try:
        #     #Somente se for mensagem privada e digitou um comando interno.
        #     if comando_interno_valido(message): 
        #         comando = message.content.split()[0]
        #         await comandos_internos[comando](message)
        #     except Exception as ex:
        #         print(ex)

        await dm_service(bot).handle_private_message(message)
    else:
        await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Hummm, não conheço esse comando, na dúvida manda um .help pra ver os comandos')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(bot.latency * 1000, 0)))

def comando_interno_valido(message):
    #o comando interno tem que ser sempre a primeir palavra
    primeira_palavra = message.content.split()[0]

    return primeira_palavra in comandos_internos.keys()

# comandos_internos = {
#     'coin': get_times,
#     'goobe':
# }

bot.run(os.getenv('DISCORD-TOKEN'))