import discord
from discord.ext import commands
from Services.ninegag_service import ninegag_service

class ninegag_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = ninegag_service()

    @commands.command(pass_context=True, aliases=['9gag'])
    async def meme(self, ctx):
        meme = await self.service.obter_posts();

        embed = discord.Embed(title = '9gag', description = meme['titulo'], color = discord.Colour.blue())
        embed.set_image(url = meme['url'])

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ninegag_cog(bot))