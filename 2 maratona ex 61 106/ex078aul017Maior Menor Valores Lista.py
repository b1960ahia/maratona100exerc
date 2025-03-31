'''lista = []
mai = 0
men = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o  valor pos {c}: ')))
    if c == 0:
         mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
            if lista[c] < men:
                men = lista[c]
print(f'Vc digitou os valores {lista}')
print(f'O maior valor foi {mai} na posição :',end='')
for c, v in enumerate(lista):
    if v == mai:
        print(f'{c}...',end='')
print()
print(f'O menor valor foi {men} na posição :',end='')
for c, v in enumerate(lista):
    if v == men:
        print(f'{c}...',end='')
print()'''
lista = [int(input('Digite o 1º valor: ')),
int(input('Digite o 2º valor: ')),
int(input('Digite o 3º valor: ')),
int(input('Digite o 4º valor: ')),
int(input('Digite o 5º valor: '))]
print(f'Os valores digitados foram: {lista}')
for c, v in enumerate(lista):
        print(f'Encontrei o valor \033[31;1m{v}\033[m na posição \033[31;1m{c}\033[m!')
print(f'O maior valor é \033[31;1m{max(lista)}\033[m e o menor valor é \033[31;1m{min(lista)}\033[m')



