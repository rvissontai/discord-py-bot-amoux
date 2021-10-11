import discord
from discord.ext import commands
import pyttsx3

from Services.lerolero_service import lerolero_service

class lerolero_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = lerolero_service()

    @commands.command(pass_context=True, aliases=['lero'])
    async def frase_aleatoria(self, ctx):
        frase_aleatoria = await self.service.obter_nova_frase();
        await ctx.send(frase_aleatoria)

    @commands.command(pass_context=True)
    async def dilma(self, ctx):
        frase_aleatoria = await self.service.obter_frase_dilma()
        await ctx.send(frase_aleatoria)


    async def enviar_audio(self, ctx, frase_aleatoria):
        canal = ctx.message.author.voice.channel

        if not canal:
            await ctx.send("Você não está conectado a um canal de voz.")
            return
        
        channel = ctx.author.voice.channel
        await channel.connect()

        try:
            engine = pyttsx3.init()
            engine.setProperty('rate',180)
            engine.save_to_file(frase_aleatoria, 'speech.mp3')
            engine.runAndWait()

            audio_source = discord.FFmpegPCMAudio('speech.mp3')

            await ctx.voice_client.play(audio_source, after=lambda e: print('Player error: %s' % e) if e else None)
            
        except Exception as e:
            print(e)

        await ctx.send(frase_aleatoria)
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(lerolero_cog(bot))