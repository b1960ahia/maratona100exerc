from random import randint
computador = randint(0, 25)
print('Sou o computador. Pensei um numero entre 0 e 10.')
print('Sera que vc adivinha o numero? ')
acertou = ''
palpite = 0# (facilitador)#
while not acertou:
    jogador = int(input('Qual seu palpite?'))
    palpite += 1# (facilitador)#
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('menos...tente mais uma vez')# (facilitador)#
print('Parabens! 🧑‍vc acertou com {} tentativas!!👍'.format(palpite))#(facilitador)


