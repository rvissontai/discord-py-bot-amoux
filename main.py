import discord 
import os

from discord.ext.commands.core import guild_only
from discord.ext import commands, tasks

from database import iniciar_database
from settings import *

from Cogs.barrel import *
from Services.dm_service import dm_service

bot = commands.Bot(command_prefix = ["?", "."], intents=discord.Intents().all())

iniciar_database()

@bot.event
async def on_ready():
    bot.load_extension("Cogs.goobee_teams_cog")
    bot.load_extension("Cogs.vitreo_telnet_cog")
    #bot.load_extension("Cogs.cadmus_coins_cog")
    bot.load_extension("Cogs.sinacor_cog")
    bot.load_extension("Cogs.central_risco_cog")
    bot.load_extension("Cogs.lerolero_cog")
    bot.load_extension("Cogs.ninegag_cog")

    print('Bot está pronto')

    await bot.change_presence(activity=discord.Game(name="jogo da vida"))
    

@bot.event
async def on_message(message):
    print(str(message.author) + ' enviou uma mensagem')

    if message.author.bot:
        return

    private_message = message.author.dm_channel is not None and message.channel.id == message.author.dm_channel.id

    if private_message: 
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


bot.run(os.getenv('DISCORD-TOKEN'))