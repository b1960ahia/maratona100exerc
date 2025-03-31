'''from random import randint
comp = randint(0, 5) #faz o computar escolher aleatoriamente
print('-_-' * 20)
print('Vou pensar em um numero entre 0 e 5, tente advinhar...')
print('-_-' * 20)
jog = int(input("Em que numero eu pensei?")) # jogador tenta adivinhar
if jog == comp:
    print('Parabens! Vc me venceu')
else:
    print('Ganhei! pensei no numero {} e nao no {}'.format(comp, jog))'''
from random import randint
from time import sleep
computador = randint (1, 25)
print('Pensarei um numero entre 1 e 25, tente advinhar...')
jogador = int(input('Em que numero eu pensei?'))
print('processando...')
sleep(2)
if jogador == computador:
    print('\033[32;40mParabens vc me venceu\033[m')
else:
    print('\033[31;40mGanhei! Pensei no numero {} e nao no {}\033[m'.format(computador, jogador))


