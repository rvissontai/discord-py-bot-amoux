import discord
from discord.ext import commands
from discord.utils import get
from Services.youtube_service import youtube_service

class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['join'])
    async def entrar(self, ctx, *, url):
        canal = ctx.message.author.voice.channel

        if not canal:
            await ctx.send("Você não está conectado a um canal de voz.")
            return
        
        channel = ctx.author.voice.channel
        await channel.connect()

        # voz = get(bot.voice_clients, guild=ctx.guild)

        # if voz and voz.is_connected():
        #     await voz.move_to(canal)
        # else:
        #     voice = await canal.connect()
        
        # await voice.disconnect()
        
        # if voice and voice.is_connected():
        #     await voice.move_to(canal)
        # else:
        #     voice = await canal.connect()

        #     channel = ctx.author.voice.channel
        #     await channel.connect()

        try:
            async with ctx.typing():
                player = await youtube_service.from_url(url, loop=False, stream=False)
                ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        except Exception as e:
            print(e)

        await ctx.send('Now playing: {}'.format(player.title))


    @commands.command(pass_context=True, aliases=['quit'])
    async def sair(self, ctx, *args):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(voice(bot))
