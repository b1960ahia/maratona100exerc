'''viagem = float(input('Qual a distancia em km da viagem?:'))
print('VAMOS VER O CUSTO DA SUA VIAGEM? ')
if viagem <= 200:
    custo = viagem * 0.50
else:
    custo = viagem * 0.45
print('O preço da passagem sera R${:.2f}'.format(custo))'''
viagem = float(input('Qual a distancia em Km?: '))
print('Vc vai iniciar uma viagem de {}km'.format(viagem))
curta = viagem * 0.50
longa = viagem * 0.45
if viagem <= 200:
    print('Custo da viagem e R$', curta)
else:
    print('Custo da viagem e R$', longa)
print('Boa viagem!')
