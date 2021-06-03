import argparse

class CustomArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super(CustomArgumentParser, self).__init__(*args, **kwargs)

        self.error_message = ''

    def error(self, message):
        self.error_message = message

    def parse_args(self, *args, **kwargs):
        # catch SystemExit exception to prevent closing the application
        result = None
        try:
            result = super().parse_args(*args, **kwargs)
        except SystemExit:
            pass
        return result

def string_para_args_parse(*args):
    comandos = []

    for arg in args:  
        comandos.append(arg)

    if len(comandos) % 2 != 0:
        return;

    response = []

    index = 0

    while index < len(comandos):
        response.append(comandos[index] + ' ' + comandos[index+1])
        index+=2

    return response