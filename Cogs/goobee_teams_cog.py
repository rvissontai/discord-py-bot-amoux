import discord
import datetime

from discord.ext import commands, tasks
from Services.goobee_teams_service import goobe_teams_service
from Common.Enum.enum_sentimento import sentimento
from Common.Enum.enum_humor_response import humor_response
from Common.Enum.enum_daily_response import daily_response
from discord.utils import get

class goobee_teams(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.service = goobe_teams_service(self.bot)
        self.aviso_informe_humor.start()
        

    @tasks.loop(seconds=30.0)
    async def aviso_informe_humor(self):
        if datetime.datetime.now().hour < 13:
            return

        executou_hoje = await self.service.task_informe_humor_executou_hoje()

        if(executou_hoje):
            return

        membros = []
        texto = ''
        usuarios = await self.service.obter_usuarios_que_nao_informaram_humor()

        if usuarios is None or len(usuarios) == 0:
            await self.service.task_informe_humor_adicionar()
            return

        for user in usuarios:
            member = get(self.bot.get_all_members(), id=int(user.idDiscord))
            membros.append(member)
            texto = member.mention + ', '

        canal = await self.service.encontrar_canal('Alcateia')

        if canal is None:
            return

        if len(membros) > 1:
            await canal.send(texto + " como vocês estão se sentindo hoje?")
        else:
            await canal.send(texto + " como está se sentindo hoje?")

        await self.service.task_informe_humor_adicionar()




    @commands.command(pass_context=True, aliases=['ta'])
    async def testeaviso(self, ctx):
        canal = await self.service.encontrar_canal('Rafael Vissontai')

        await canal.send("Mensagem enviada da task")
    

    @commands.command(pass_context=True, aliases=['f', 'F'])
    async def feliz(self, ctx):
        await self.add_humor(ctx, sentimento.feliz.value)

    @commands.command(pass_context=True, aliases=['b', 'B'] )
    async def bom(self, ctx):
        await self.add_humor(ctx, sentimento.bom.value)

    @commands.command(pass_context=True, aliases=['n', 'N'])
    async def nao_tao_bom(self, ctx):
        await self.add_humor(ctx, sentimento.nao_tao_bom.value)

    @commands.command(pass_context=True, aliases=['t', 'T'])
    async def triste(self, ctx):
        await self.add_humor(ctx, sentimento.triste.value)

    @commands.command(pass_context=True, aliases=['d', 'D'])
    async def daily(self, ctx):
        #Enviar uma mensagem para informar o usuário que o humor está sendo modificado.
        mensagem = await ctx.send('Definindo daily...')

        #Modificar daily como realizada
        response = await self.service.realizar_daily(ctx.author.id)

        #Definir a mensagem a ser exibida com base no response
        if(response == daily_response.sucesso):
            await mensagem.edit(content = 'Daily definida como realizada!')
            return
        
        if (response == daily_response.erro_realizar_daily):
            await mensagem.edit(content = 'Cara alguma coisa errada não ta certa, não consegui realizar a daily. ):')
            return
        
        if (response == daily_response.erro_autenticacao):
            await mensagem.edit(content = 'Cara deu alguma coisa errada com sua autenticação ):')
            return

        if (response == daily_response.erro_usuario_nao_existe):
            await mensagem.edit(content = 'Você ainda não me informou suas credenciais, enviei uma mensagem privada pra você, é só seguir as instruções por lá.')
            await ctx.author.send('Agora é só me falar seu email e senha em uma única mensagem beleza? fica tranquilo que não sou X9. \n ex: -s goobe -l eu@email.com -p senha123')     
            return



    async def add_humor(self, ctx, id_sentimento):
        #Enviar uma mensagem para informar o usuário que o humor está sendo modificado.
        mensagem = await ctx.send('Definindo humor...')

        #Modificar o humor do usuário
        response = await self.service.add_humor(ctx.author.id, id_sentimento)

        #Definir a mensagem a ser exibida com base no response
        if(response == humor_response.sucesso):
            await mensagem.edit(content = ctx.author.mention + ', seu humor foi alterado!')
            return
        
        if (response == humor_response.erro_alterar_humor):
            await mensagem.edit(content = format(ctx.author.mention) + ', alguma coisa errada não ta certa, não consegui alterar o humor ):')
            return
        
        if (response == humor_response.erro_autenticacao):
            await mensagem.edit(content = format(ctx.author.mention) + ', cara deu alguma coisa errada com sua autenticação ):')
            return

        if (response == humor_response.erro_usuario_nao_existe):
            await mensagem.edit(content = 'Você ainda não me informou suas credenciais, enviei uma mensagem privada pra você, é só seguir as instruções por lá.')
            await ctx.author.send('Agora é só me falar seu email e senha em uma única mensagem beleza? fica tranquilo que não sou X9. \n ex: -s goobe -l eu@email.com -p senha123')     
            return

        if (response == humor_response.timeout):
            await mensagem.edit(content = 'A API do goobe não está respondendo, timeout ):')
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

    @commands.command(pass_context=True, aliases=['hh'])
    async def hug(self, ctx):
        await ctx.send("hugs {}".format(ctx.message.author.mention()))

def setup(bot):
    bot.add_cog(goobee_teams(bot))