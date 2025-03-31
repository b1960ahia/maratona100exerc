'''n = 0
cont = 0
while True:
    print('~'*50)
    n = int(input('\033[40;32;7;1m Escolha um numero e mostre sua tabuada\033[m \033[31;1m[negativo parar]\033[m : '))
    print('~'*50)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n * cont}')
print('Programa de tabuada encerrado🧗')
print('Parabens vc Conseguiu!!!💪')'''

print('{:=^20}'.format('TABUADA'))
num = 0
cont = 0
while True:
    num = int(input('Escolha um numero para ver a tabuada: '))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')
    print('Programa concluido')






