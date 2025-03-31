from time import sleep
n1 = int(input(' 1º numero: '))
n2 = int(input(' 2º numero: '))
opção = 0
while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('\033[31;1m Qual e a sua opção?\033[m'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os numeros de novo.')
        n1 = int(input('1º numero: '))
        n2 = int(input('2º numero: '))
    elif opção == 5:
        if opção != 0:
            print('\033[35;1m Finalizando...\033[m')
    else:
        print('Opção invalida. Tente de novo')
    print('=-=' * 10)
    sleep(2)
print('\033[41;30;1m Fim do programa!\033[m'.format(opção))



