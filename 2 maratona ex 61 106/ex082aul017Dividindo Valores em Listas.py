lista = []
pares = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar?: [S/N]'))
    if res in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Lista de pares {pares}')
print(f'Lista de impar{impar}')
print(f'Os valores da lista : {lista}: ')
