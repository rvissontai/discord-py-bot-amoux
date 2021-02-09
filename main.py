import discord 
import requests
import json
import argparse
import os

from discord.ext import commands
from database import iniciar_database
from parses.coins_parser import coins_parser
from settings import *

from Cogs.barrel import *

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
    print(message)
    # try:
    #     #Somente se for mensagem privada e digitou um comando interno.
    #     if message.channel.id == message.author.dm_channel.id and comando_interno_valido(message): 
    #         comando = message.content.split()[0]
    #         await comandos_internos[comando](message)
    # except Exception as ex:
    #      print(ex)

    # try:
    #     if message.channel.id == message.author.dm_channel.id: 
    #         credenciais = message.content.split()

    #         response = autenticar(credenciais[0], credenciais[1])

    #         if(response.status_code == 200):
    #             try:
    #                 user = Usuarios.get(Usuarios.idDiscord == message.author.id)
    #                 Usuarios.update(login = credenciais[0], senha = credenciais[1]).where(Usuarios.idDiscord == message.author.id).returning(Usuarios)
    #             except Usuarios.DoesNotExist:
    #                 Usuarios.insert(idDiscord=message.author.id, login=credenciais[0], senha=credenciais[1]).execute()

    #             await message.channel.send('Beleza, consegui logar aqui, agora é só ir no chat geral e mudar seu humor.')
    #         else:
    #             await message.channel.send('Não foi possível autenticar, tem certeza que me passou as informações certas?')
    # except:
    #     print(message)

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(bot.latency * 1000, 0)))

@bot.command(pass_context=True)
async def times(ctx):
    print('time')
    # comando = params['c']
    # response = await comandos_internos[comando](ctx)

    # if(response.status_code == 200):
    #     await ctx.send(response.text)
    # else:
    #     await ctx.send('Erro listar times')

async def comando_times(message):
    args = message.split()
    print('executanto comando times')

# def comando_interno_valido(message):
#     #o comando interno tem que ser sempre a primeir palavra
#     primeira_palavra = message.content.split()[0]

#     return primeira_palavra in comandos_internos.keys()

# comandos_internos = {
#     'list': get_times
# }

bot.run(os.getenv('DISCORD-TOKEN'))