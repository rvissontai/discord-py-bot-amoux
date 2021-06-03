from telnetlib import Telnet
from datetime import datetime
from database import LastestCleaning

import os
class vitreo_telnet_service():
    def __init__(self, bot):
        self.bot = bot
        self.host = os.getenv('VITREO-TELENT-HOST')
        self.port = 11211#os.getenv('VITREO-TELNET-PORT')
        self.timeout = 100#os.getenv('VITREO-TELENT-TIMEOUT')

    async def limpar_cache(self):
        try:        
            with Telnet(self.host, self.port, self.timeout) as session:
                session.write(b"flush_all\n")
                session.write(b"quit\n")

            #LastestCleaning.insert(data=datetime.now()).execute()

            return True
        except Exception as e:
            print(e)
            return False

    