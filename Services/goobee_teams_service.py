import requests
import json
from database import Usuarios
from datetime import timezone, datetime
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pprint
from Common.Enum.enum_humor_response import humor_response

class goobe_teams_service():
    def __init__(self, bot):
        self.bot = bot
        self.url_auth = os.getenv('GOOBEE-URL') + os.getenv('GOOBE-ENDPOINT-AUTH')
        self.url_humor = os.getenv('GOOBEE-URL') + os.getenv('GOOBE-ENDPOINT-HUMOR')
        self.url_daily = os.getenv('GOOBEE-URL') + os.getenv('GOOBEE-ENDPOINT-DAILY')

    async def autenticar(self, user, senha):
        return requests.post(self.url_auth, data=None, json={'usuario': user, 'senha': senha })

    async def add_humor(self, idDiscord, id_sentimento):
        try:
            user = Usuarios.get(Usuarios.idDiscord == idDiscord)
            response = await self.autenticar(user.login, user.senha)
            
            if(response.status_code == 200):
                sucesso_response = json.loads(response.text)

                header = { 'Authorization': 'Bearer ' + sucesso_response["token"] }
                param = {
                    'idPessoa': sucesso_response["idPessoa"],
                    'idResponsavelCriacao': sucesso_response["id"],
                    'sentimento': id_sentimento
                }

                humorResponse = requests.post(self.url_humor, json=param, headers=header)

                if(humorResponse.status_code == 200):
                    return humor_response.sucesso

                return humor_response.erro_alterar_humor
            else:
                return humor_response.erro_autenticacao

        except Usuarios.DoesNotExist:
            return humor_response.erro_usuario_nao_existe

        except Exception as e:
            print(e)

    async def realizar_daily(self, ctx) :
        mensagem = await ctx.send('Definindo daily...')

        try:
            user = Usuarios.get(Usuarios.idDiscord == ctx.author.id)
            response = await self.autenticar(user.login, user.senha)
            
            if(response.status_code == 200):
                sucesso_response = json.loads(response.text)

                header = { 'Authorization': 'Bearer ' + sucesso_response["token"] }
                param = {
                    'dia': datetime.now().isoformat(),
                    'idTime': sucesso_response["idsTimes"][0],
                    'idResponsavelRegistro': sucesso_response["idPessoa"],
                    'observacao':''
                }

                response = requests.post(self.url_daily, json=param, headers=header)

                if(response.status_code == 200):
                    await mensagem.edit(content = 'Daily definida como realizada!')
                else :
                    await mensagem.edit(content = 'Cara alguma coisa errada não ta certa, não consegui realizar a daily. ):')

            else:
                await ctx.author.send('Cara deu alguma coisa errada com sua autenticação ):')                

        except Usuarios.DoesNotExist:
            await ctx.author.send('Agora é só me falar seu email e senha em uma única mensagem beleza? fica tranquilo que não sou X9. \n ex: -s goobe -l eu@email.com -p senha123')     
        except Exception as e:
            await mensagem.edit(content = 'Cara alguma coisa errada não ta certa, não consegui realizar a daily ):')
            print(e)

    async def encriptar_autenticacao(self, user, password):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1366,768")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}

        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options, desired_capabilities=caps)

        driver.get('https://teams.goobee.com.br/login')
        
        input_email = driver.find_element_by_id("mat-input-0")
        input_password = driver.find_element_by_id("mat-input-1")
        button_login = driver.find_element_by_class_name("submit-button")

        input_email.send_keys(user)
        input_password.send_keys(password)

        button_login.click()

        logs = driver.get_log("performance")

        try:
            return await self.process_browser_logs_for_network_events(logs)
        except Exception as ex:
            print(ex)

        

    async def process_browser_logs_for_network_events(self, logs):
        result = {}
        for entry in logs:
            log = json.loads(entry["message"])["message"]

            if log["method"] != "Network.requestWillBeSent":
                continue

            if "params" not in log:
                continue

            if "request" not in log["params"]:
                continue

            if "postData" not in log["params"]["request"]:
                continue

            postData = log["params"]["request"]["postData"]

            if "usuario" not in postData or "senha" not in postData:
                continue

            jsonUser = json.loads(postData)

            result = {
                'login': jsonUser["usuario"],
                'password': jsonUser["senha"]
            }

            break

        return result

            # if log["method"] == "Network.requestWillBeSent":
            #     if "params" in log:
            #         param = log["params"]
            #         if "request" in param:
            #             request = param["request"]
            #             if "postData" in request:
            #                 postData = request["postData"]
            #                 if "usuario" in postData and "senha" in postData:
            #                     jsonUser = json.loads(postData)
            #                     result.append('user: ' + jsonUser["usuario"])
            #                     result.append('senha: ' + jsonUser["senha"])
        
        
