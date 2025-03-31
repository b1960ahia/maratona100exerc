print('{:=^40}'.format(' LOJAS BARATÃO '))
totc = totMil = menor = cont = 0
barato = ''
while True:
    nomep = str(input('Nome do produto : '))
    precop = float(input('Preço do produto é: R$ '))
    cont += 1
    totc += precop
    if precop > 1000:
        totMil += 1
    if cont == 1 or precop < menor:
        menor = precop
        barato = nomep
    '''if cont == 1:
        menor = precop
        barato = nomep
    else:
        if precop < menor:
            menor = precop
            barato = nomep'''
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O produto mais barato custa {menor} é {barato}')
print(f'{totMil} produtos custa mais de R$ 1000')
print(f'O valor total foi {totc}')
print('{:=^40}'.format('FIM DO PROGRAMA'))
