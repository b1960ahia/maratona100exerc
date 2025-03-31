from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opcoes
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual e a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 14)
print('Opcao do computador {}'.format(itens[computador]))
print('Opcao do jogador {}'.format(itens[jogador]))
print('-=' * 14)
if computador == 0: #computador jogou pedra
   if jogador == 0:
    print('empate')
   elif jogador == 1:
    print('Jogador vence')
   elif jogador == 2:
    print('computador vence')
else:
    print('Jogada invalida')
if computador == 1:# computador jogou papel
   if jogador == 0:
    print('computador vence')
   elif jogador == 1:
    print('empate')
   elif jogador == 2:
    print('jogador vence')
else:
    print('Jogada invalida')
if computador == 2: #computador jogou Tesoura
   if jogador == 0:
    print('jogador vence')
   elif jogador == 1:
    print('computador vence')
   elif jogador == 2:
    print('empate')
else:
    print('jogada invalida')

