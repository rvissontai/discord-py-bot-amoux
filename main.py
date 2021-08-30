import time
import discord 
import os
import asyncio
#import aioschedule

from discord.ext.commands.core import guild_only
from discord.ext import commands, tasks

from database import iniciar_database
from settings import *

from Cogs.barrel import *
from Services.dm_service import dm_service
import json

bot = commands.Bot(command_prefix = ["?", "."], intents=discord.Intents().all())

iniciar_database()

@bot.event
async def on_ready():
    bot.load_extension("Cogs.goobee_teams_cog")
    bot.load_extension("Cogs.vitreo_telnet_cog")
    bot.load_extension("Cogs.cadmus_coins_cog")
    bot.load_extension("Cogs.sinacor_cog")
    bot.load_extension("Cogs.central_risco_cog")

    print('Bot está pronto')

    await bot.change_presence(activity=discord.Game(name="jogo da vida"))

    # Opening JSON file
    # f = open('response.json', encoding="utf8")
    # fnovo = open("inserts.txt", "w")

    # data = json.load(f)
    
    # inserts = []

    # for i in data:
    #     fnovo.write(f"INSERT INTO api_sisfinance_simulator.tb_participacao_ativo (exchange_code, ativo, ativo_legado, percentual, tipo_mercado, mercado, ds_investimento, dt_inclusao) VALUES(120948, '{i['ativo']}', '{i['ativoLegado']}', {i['percentual']}, '{i['tipoMercado']}', '{i['mercado']}', '{i['ds_Investimento']}', now()); \n")
    
    # # Closing file
    # f.close()
    # fnovo.close()



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
    teste = ctx.guild.members
    await ctx.send('Pong! {0}ms'.format(round(bot.latency * 1000, 0)))


# class MyHelpCommand(commands.MinimalHelpCommand):
#     async def send_pages(self):
#         destination = self.get_destination()
#         e = discord.Embed(color=discord.Color.blurple(), description='')

#         for page in self.paginator.pages:
#             e.description += page + "\n"

#         await destination.send(embed=e)

# bot.help_command = MyHelpCommand()

def comando_interno_valido(message):
    pass
    #o comando interno tem que ser sempre a primeir palavra
    # primeira_palavra = message.content.split()[0]

    # return primeira_palavra in comandos_internos.keys()

# comandos_internos = {
#     'coin': get_times,
#     'goobe':
# }

bot.run(os.getenv('DISCORD-TOKEN'))


