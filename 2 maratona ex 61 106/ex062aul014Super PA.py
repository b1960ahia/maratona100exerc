print('=\033[40;1mGERADOR DE PA\033[m=')
print('-=' * 10)
primeiro = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total +=mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termo vc quer mostrar a mais?:'))
print('\033[42;30;1mProgressão finalizada com sucesso com {} termos\033[m'.format(total))
