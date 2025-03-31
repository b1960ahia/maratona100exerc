valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print(' Valor adicionado com sucesso!')
    else:
        print('Valor duplicado,não vou adicionar.')
    resp = str(input('Quer continuar? S/N'))
    if resp in 'Nn':
        break
print(f'Vc digitou os valores {sorted(valores)}')
#print(sorted(valores))