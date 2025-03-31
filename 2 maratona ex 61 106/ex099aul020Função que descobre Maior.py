from time import sleep
def maior(*n):
    cont = maior = 0
    print('<>' * 20)
    print('\nAnalisando os valores... ')
    for valor in n:
        print(f'\033[33;40m{valor}\033[m',end=' ', flush=True)
        sleep(1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram analisados {cont} valores')
    print(f'O maior valor foi \033[31;40m{maior}\033[m')


maior(3, 9, 3, 6, 8,)
maior(6, 4)
maior(1, 4, 6, 22)
maior(6, 45, 2)

