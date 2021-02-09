import argparse

coins_parser = argparse.ArgumentParser(description='Enviar coins para alguém')
coins_parser.add_argument('--para', help='E-mail de quem vai receber as coins')
coins_parser.add_argument('--quantidade', type=int, help='Número de coins que serão enviadas.')
coins_parser.add_argument('--mensagem', help='Uma simples mensagem que será enviada para o destinatário.')