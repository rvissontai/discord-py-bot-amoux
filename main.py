import discord 
import requests
import json
import argparse
import os

from discord.ext import commands
from database import iniciar_database
from parses.coins_parser import coins_parser
from settings import *

from Services.goobee_teams_service import goobe_teams_service
from database import Usuarios

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
    print(str(message.author) + ' enviou uma mensagem')

    if message.author.bot:
        return

    # try:
    #     #Somente se for mensagem privada e digitou um comando interno.
    #     if message.channel.id == message.author.dm_channel.id and comando_interno_valido(message): 
    #         comando = message.content.split()[0]
    #         await comandos_internos[comando](message)
    # except Exception as ex:
    #      print(ex)
    private_message = message.author.dm_channel is not None and message.channel.id == message.author.dm_channel.id

    if private_message: 
        credenciais = message.content.split()

        service = goobe_teams_service(bot)

        response = await service.autenticar(credenciais[0], credenciais[1])

        if(response.status_code == 200):
            try:
                user = Usuarios.get(Usuarios.idDiscord == message.author.id)
                Usuarios.update(login = credenciais[0], senha = credenciais[1]).where(Usuarios.idDiscord == message.author.id).returning(Usuarios)
            except Usuarios.DoesNotExist:
                Usuarios.insert(idDiscord=message.author.id, login=credenciais[0], senha=credenciais[1]).execute()

            await message.channel.send('Beleza, consegui logar aqui, agora é só ir no chat geral e mudar seu humor.')
        else:
            await message.channel.send('Não foi possível autenticar, tem certeza que me passou as informações certas?')
    else:
        await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Hummm, não conheço esse comando, na dúvida manda um .help pra ver os comandos')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}ms'.format(round(bot.latency * 1000, 0)))

# def comando_interno_valido(message):
#     #o comando interno tem que ser sempre a primeir palavra
#     primeira_palavra = message.content.split()[0]

#     return primeira_palavra in comandos_internos.keys()

# comandos_internos = {
#     'list': get_times
# }

bot.run(os.getenv('DISCORD-TOKEN'))