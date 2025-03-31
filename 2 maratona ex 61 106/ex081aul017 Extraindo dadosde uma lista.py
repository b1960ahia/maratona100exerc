valor = []
while True:
    valor.append(int(input('Digite um numero: ')))
    res = str(input('Quer continuar? [S/N]'))
    if res in 'Nn':
        break
print(f'Vc digitou {len(valor)} numeros')
valor.sort(reverse=True)
print(f'Em ordem decrescente {valor}')
if 5 in valor:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 nao foi encontrado')




