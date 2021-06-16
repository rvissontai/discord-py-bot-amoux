import discord
from discord.ext import commands
from Services.goobee_teams_service import goobe_teams_service
from Common.Enum.enum_sentimento import sentimento
from Common.Enum.enum_humor_response import humor_response

class goobee_teams(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = goobe_teams_service(self.bot)

    @commands.command(pass_context=True, aliases=['f'])
    async def feliz(self, ctx):
        await self.add_humor(ctx, sentimento.feliz.value)

    @commands.command(pass_context=True, aliases=['n'] )
    async def neutro(self, ctx):
        await self.add_humor(ctx, sentimento.neutro.value)

    @commands.command(pass_context=True, aliases=['i'])
    async def irritado(self, ctx):
        await self.add_humor(ctx, sentimento.irritado.value)

    @commands.command(pass_context=True, aliases=['d'])
    async def daily(self, ctx):
        await self.service.realizar_daily(ctx)

    async def add_humor(self, ctx, id_sentimento):
        #Enviar uma mensagem para informar o usuário que o humor está sendo modificado.
        mensagem = await ctx.send('Definindo humor...')

        #Modificar o humor do usuário
        response = await self.service.add_humor(ctx.author.id, id_sentimento)

        #Definir a mensagem a ser exibida com base no response
        if(response == humor_response.sucesso):
            await mensagem.edit(content = 'Seu humor foi alterado!')
            return
        
        if (response == humor_response.erro_alterar_humor):
            await mensagem.edit(content = 'Cara alguma coisa errada não ta certa, não consegui alterar o humor ):')
            return
        
        if (response == humor_response.erro_autenticacao):
            await mensagem.edit(content = 'Cara deu alguma coisa errada com sua autenticação ):')
            return

        if (response == humor_response.erro_usuario_nao_existe):
            await mensagem.edit(content = 'Você ainda não me informou suas credenciais, enviei uma mensagem privada pra você, é só seguir as instruções por lá.')
            await ctx.author.send('Agora é só me falar seu email e senha em uma única mensagem beleza? fica tranquilo que não sou X9. \n ex: -s goobe -l eu@email.com -p senha123')     
            return
        

    @commands.command(pass_context=True)
    async def times(self, ctx):
        print('time')
        # comando = params['c']
        # response = await comandos_internos[comando](ctx)

        # if(response.status_code == 200):
        #     await ctx.send(response.text)
        # else:
        #     await ctx.send('Erro listar times')

    async def comando_times(self, message):
        args = message.split()
        print('executanto comando times')

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