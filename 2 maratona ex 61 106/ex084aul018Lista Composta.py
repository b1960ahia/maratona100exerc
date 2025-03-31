temp = []
lista = []
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(lista) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    lista.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar: S/N'))
    if resp in 'Nn':
        break
#print(f'Os dados foram {lista}: ')
#print(f'Foram cadastradas {len(lista)} pessoas')
#print(f'O menor peso foi {men} kg')
#print(f'O maior peso foi {mai} kg')
print(f'Vc cadastrou {len(lista)} pessoas')
print(f'A pessoa maior peso tem {mai} kg. Peso de ',end='')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}]',end='')
print()
print(f'A pessoa com menor peso tem {men} kg. Peso de ',end='')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}]',end='')
print()