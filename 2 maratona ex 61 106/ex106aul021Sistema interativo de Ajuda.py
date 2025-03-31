
from time import sleep
'''c = ('\033[m',      sem cores
     '\033[0;30;41m',  vermelho
     '\033[0;30;42m',  verde
     '\033[0;30;43m',  amarelo
     '\033[0;30;44m',  azul
     '\033[0;30;45m',  roxo
     '\033[7;30m'      branco
     );'''
def ajuda(com):
    titulo(f'\033[0;30;43mAcessando Manual do Comando\033[m \033[0;30;45m{com}\033[m')
    help(com)
    sleep(2)

def titulo(msg, cor=0):
    #tam = len(msg)
    #print(c[cor], end='')
    print('~'*28)
    print(f' {msg}')
    print('~'*28)
    #print(c[0], end='')
    sleep(2)

comando = ''
while True:
    titulo('\033[0;30;42mSISTEMA DE AJUDA PyHELp\033[m')
    comando = str(input(' Função ou Biblioteca >> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('\033[0;30;44mATE LOGO\033[m')
