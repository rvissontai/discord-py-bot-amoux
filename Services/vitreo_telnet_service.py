from telnetlib import Telnet
import os

host = os.getenv('VITREO-TELENT-HOST')
port = os.getenv('VITREO-TELENT-PORT')
timeout = os.getenv('VITREO-TELENT-TIMEOUT')

class vitreo_telnet_service():
    def __init__(self, bot):
        self.bot = bot

    async def limpar_cache(self):
        try:        
            with Telnet(host, port, timeout) as session:
                session.write(b"flush_all\n")
                session.write(b"quit\n")

            return True
        except Exception as e:
            print(e)
            return False

    