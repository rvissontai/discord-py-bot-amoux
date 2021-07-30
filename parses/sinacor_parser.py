import argparse
from Util.parser_helper_util import CustomArgumentParser

class sinacor_parser():
    def __init__(self):
        self.sinacor_parser = CustomArgumentParser(description='Sinacor')

        self.sinacor_parser.add_argument('-s', '--status', help='Verificar se o sinacor está aberto ou fechado', action='store_true')
        self.sinacor_parser.add_argument('-a', '--abrir', help='Abrir o sinacor', action='store_true')
        self.sinacor_parser.add_argument('-f', '--fechar', help='Fechar o sinacor', action='store_true')


    def obter_parser(self):
        return self.sinacor_parser
        

    def obter_ajuda(self):
        return [
            '\t-s --status \t Verificar se o sinacor está aberto ou fechado.\n', 
            '\t-a --abrir  \t Abrir o sinacor\n', 
            '\t-f --fechar \t Fechar o sinacor'
        ]

