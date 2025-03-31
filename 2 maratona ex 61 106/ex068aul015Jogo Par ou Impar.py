'''print('='*25)
print('Vamos jogar Par ou Impar')
print('='*25)
from random import randint
v = 0
while True:
    jogador = int(input('Escolha um numero? :'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar?: [P/I]')).strip().upper()[0]
    print(f'VC jogou {jogador} e o computador {computador}. Total {total} ')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('VOCE PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Vc venceu {v} vezes.')'''

