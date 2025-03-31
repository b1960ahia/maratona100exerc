primeiro = int(input(' Primeiro Termo: '))
razao = int(input('Razao: '))
decimo = primeiro + ( 10 - 1) * razao
for c in range(primeiro,decimo + razao, razao):
    print('{}' .format(c),end=' ')
print('FIM')

'''primeiro = int(input('Digite o 1º termo: '))
razao = int(input('Razao: '))
vigesimo = primeiro + (20 - 1) * razao
print('\033[31m{:=^10}'.format('PA'))
for c in range(primeiro, vigesimo + razao, razao):
        print('{}'.format(c),end=' ')'''