from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('<>' * 20)
    print(f'Contagem do {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ',flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ',flush=True)
            sleep(0.5)
            cont -= p
    print(' FIM ')


contador(1, 10, 1)
contador(10, 0, 2)
print('<>'* 20)
print('Personalise a contagem:')
ini = int(input('inicio:'))
fim = int(input('fim:   '))
pas = int(input('passo: '))
contador(ini, fim, pas)
#contador(-2, 10, -2)



