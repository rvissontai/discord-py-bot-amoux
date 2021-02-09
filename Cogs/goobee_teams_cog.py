import discord
from discord.ext import commands
from Services.goobee_teams_service import goobe_teams_service

class goobee_teams(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = goobe_teams_service(self.bot)

    @commands.command(pass_context=True, aliases=['f'])
    async def feliz(self, ctx):
        await self.service.add_humor(ctx, 1)

    @commands.command(pass_context=True, aliases=['n'] )
    async def neutro(self, ctx):
        await self.service.add_humor(ctx, 2)

    @commands.command(pass_context=True, aliases=['i'])
    async def irritado(self, ctx):
        await self.service.add_humor(ctx, 3)

    @commands.command(pass_context=True, aliases=['d'])
    async def daily(self, ctx):
        await self.service.realizar_daily(ctx)

    async def get_times(self, ctx):
        pass
        # user = Usuarios.get(Usuarios.idDiscord == ctx.author.id)
        # response = autenticar(user.login, user.senha)

        # if(response.status_code == 200):
        #     sucesso_response = json.loads(response.text)

        #     header = { 'Authorization': 'Bearer ' + sucesso_response["token"] }
        #     param = {
        #         'ativo': True,
        #         'idCliente': "",
        #         'idGrupo': "",
        #         'idProjeto': "",
        #         'temperatura': ""
        #     }

        #     return requests.post('https://apiteams.goobee.com.br/api/Time/Times', json=param, headers=header)

def setup(bot):
    bot.add_cog(goobee_teams(bot))