lista = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
par = mai = col = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um numero [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]',end='')
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
    print()
print(f'A soma dos valores pares é {par}')
for l in range(0, 3):
    col += lista[l][2]
print(f'A soma dos valores da terceira coluna e {col}')
for c in range(0, 3):
    if c == 0:
        mai = lista[1][c]
    elif lista[1][c] > mai:
        mai = lista[1][c]
print(f'O maior valor da segunda linha é {mai}')
