from random import randint
from time import sleep
lista = list()
jogos = list()
print('='*38)
print('        JOGOS DE LOTERIAS        ')
print('='*38)
quant = int(input('Quantos jogos vc quer sortear?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 25)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 15:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'\033[33;40m SORTEANDO {quant} JOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('<<<<<<<<BOA SORTE>>>>>>>>>>\033[m')