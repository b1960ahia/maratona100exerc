lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if c % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Lista = {lista}')
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')
