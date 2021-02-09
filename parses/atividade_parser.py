import argparse

atividade_parser = argparse.ArgumentParser(description='Enviar coins para alguém')
atividade_parser.add_argument('--para', help='E-mail de quem vai receber as coins')
atividade_parser.add_argument('--quantidade', type=int, help='Número de coins que serão enviadas.')
atividade_parser.add_argument('--mensagem', help='Uma simples mensagem que será enviada para o destinatário.')