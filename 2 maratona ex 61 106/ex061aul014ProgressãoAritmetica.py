print('=====\033[40;1mGERADOR DE PA\033[m======')
print('-=' * 10)
primeiro = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')



