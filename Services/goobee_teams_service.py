from Util.parser_helper_util import string_para_base64, encontrar_canal_padrao
import requests
import json

from database import Usuarios
from database import HumorDiario

import datetime

import os

from Common.Enum.enum_humor_response import humor_response
from Common.Enum.enum_daily_response import daily_response
from Services.request.informar_humor_request import informar_humor_request

class goobe_teams_service():
    def __init__(self, bot):
        self.bot = bot
        self.url_auth = os.getenv('GOOBEE-URL') + os.getenv('GOOBE-ENDPOINT-AUTH')
        self.url_humor = os.getenv('GOOBEE-URL') + os.getenv('GOOBE-ENDPOINT-HUMOR')
        self.url_editar_humor = os.getenv('GOOBEE-URL') + os.getenv('GOOBE-ENDPOINT-EDITAR-HUMOR')
        self.url_daily = os.getenv('GOOBEE-URL') + os.getenv('GOOBEE-ENDPOINT-DAILY')

    async def autenticar(self, user, senha):
        return requests.post(self.url_auth, data=None, json={'usuario': user, 'senha': senha })

    async def add_humor(self, idDiscord, id_sentimento):
        try:
            user = Usuarios.get(Usuarios.idDiscord == idDiscord)
            response = await self.autenticar(user.login, user.senha)
            
            if(response.status_code != 200 or response.ok is not True):
                return humor_response.erro_autenticacao
            
            sucesso_response = json.loads(response.text)

            header = { 'Authorization': 'Bearer ' + sucesso_response["token"] }

            sentimento_diario_response = await self.obter_sentimento_diario(sucesso_response["token"], sucesso_response["idPessoa"])

            if sentimento_diario_response is None:
                param = {
                    'idPessoa': sucesso_response["idPessoa"],
                    'idResponsavelCriacao': sucesso_response["id"],
                    'sentimento': id_sentimento
                }

                humorResponse = requests.post(self.url_humor, json=param, headers=header)

                #HumorDiario
            else:
                param = {
                    'idSentimentoPessoa': sentimento_diario_response,
                    'idResponsavelCriacao': sucesso_response["id"],
                    'sentimento': id_sentimento
                }

                humorResponse = requests.put(self.url_editar_humor + sentimento_diario_response, json=param, headers=header)

            if(humorResponse.status_code != 200 or humorResponse.ok is not True):
                return humor_response.erro_alterar_humor
                
            return humor_response.sucesso
        except Usuarios.DoesNotExist:
            return humor_response.erro_usuario_nao_existe

        except Exception as e:
            print(e)
            return humor_response.erro_alterar_humor

    async def obter_sentimento_diario(self, token, id_pessoa):
        response = requests.get(
            os.getenv('GOOBEE-URL') + '/api/Home/InformaHumor', 
            params={'idPessoa': id_pessoa },
            headers= { 'Authorization': 'Bearer ' + token })

        if response.status_code != 200:
            return None

        model = json.loads(response.text)

        if model["idSentimentoPessoa"] is None:
            return None

        return model["idSentimentoPessoa"]


    async def realizar_daily(self, idDiscord) :
        try:
            user = Usuarios.get(Usuarios.idDiscord == idDiscord)
            response = await self.autenticar(user.login, user.senha)
            
            if(response.status_code == 200):
                sucesso_response = json.loads(response.text)

                header = { 'Authorization': 'Bearer ' + sucesso_response["token"] }
                param = {
                    'dia': datetime.datetime.now().isoformat(),
                    'idTime': sucesso_response["idsTimes"][0],
                    'idResponsavelRegistro': sucesso_response["idPessoa"],
                    'observacao':''
                }

                response = requests.post(self.url_daily, json=param, headers=header)

                if(response.status_code == 200):
                    return daily_response.sucesso

                return daily_response.erro_realizar_daily
            else:
                return daily_response.erro_autenticacao

        except Usuarios.DoesNotExist:
            return daily_response.erro_usuario_nao_existe
        except Exception as e:
            print(e)
            return daily_response.erro_realizar_daily

    async def encriptar_autenticacao(self, login, password):
        return {
            "login": string_para_base64(login),
            "password": string_para_base64(password)
        };
        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"

        # options = webdriver.ChromeOptions()
        # options.headless = True
        # options.add_argument(f'user-agent={user_agent}')
        # options.add_argument("--window-size=1366,768")
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--allow-running-insecure-content')
        # options.add_argument("--disable-extensions")
        # options.add_argument("--proxy-server='direct://'")
        # options.add_argument("--proxy-bypass-list=*")
        # options.add_argument("--start-maximized")
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--no-sandbox')

        # caps = DesiredCapabilities.CHROME
        # caps['goog:loggingPrefs'] = {'performance': 'ALL'}

        # driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options, desired_capabilities=caps)

        # driver.get('https://teams.goobee.com.br/login')
        
        # input_email = driver.find_element_by_id("mat-input-0")
        # input_password = driver.find_element_by_id("mat-input-1")
        # button_login = driver.find_element_by_class_name("submit-button")

        # input_email.send_keys(user)
        # input_password.send_keys(password)

        # button_login.click()

        # logs = driver.get_log("performance")

        # try:
        #     return await self.process_browser_logs_for_network_events(logs)
        # except Exception as ex:
        #     print(ex)

    # async def process_browser_logs_for_network_events(self, logs):
    #     result = {}
    #     for entry in logs:
    #         log = json.loads(entry["message"])["message"]

    #         if log["method"] != "Network.requestWillBeSent":
    #             continue

    #         if "params" not in log:
    #             continue

    #         if "request" not in log["params"]:
    #             continue

    #         if "postData" not in log["params"]["request"]:
    #             continue

    #         postData = log["params"]["request"]["postData"]

    #         if "usuario" not in postData or "senha" not in postData:
    #             continue

    #         jsonUser = json.loads(postData)

    #         result = {
    #             'login': jsonUser["usuario"],
    #             'password': jsonUser["senha"]
    #         }

    #         break

    #     return result
        
    async def enviar_notificacao_humor(self):
        canal = encontrar_canal_padrao(self.bot)

        if canal is None:
            print("Nenhum canal padrão configurado")
            return

        

    async def obter_usuarios_que_nao_informaram_humor(self):
        try:
            notificar_usuarios = []
            users = Usuarios.select().execute()

            for user in users:
                try:
                    HumorDiario.get(
                        HumorDiario.idDiscord == user.idDiscord and 
                        HumorDiario.data == datetime.date.today()
                    )
                    
                except HumorDiario.DoesNotExist:
                    notificar_usuarios.append(user)

                except Exception as e:
                    print(e)

            return notificar_usuarios

        except Exception as e:
            print(e)        
            return None