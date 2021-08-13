import argparse
from Util.parser_helper_util import CustomArgumentParser

class central_risco_parser():
    def __init__(self):
        self.central_risco_parser = CustomArgumentParser(description='Central Risco')
        
        self.central_risco_parser.add_argument('-a', '--aprovar_ordem', help='Aprovar uma ordem na central de risco e mudar status para EXECUTED', required=True)


    def obter_parser(self):
        return self.central_risco_parser
        

    def obter_ajuda(self):
        return [
            '\t-a --aprovar_ordem \t Aprovar uma ordem na central de risco e mudar status para EXECUTED.\n', 
        ]

