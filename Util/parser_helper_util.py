
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