pmaior = 0
pmenor = 0
for p in range(1, 6):
    peso = float(input('Qual e o  Peso {}ª pessoa?: '.format(p)))
    if p == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso
print('O maior peso e {}kg'.format(pmaior))
print('O menor peso e {}kg'.format(pmenor))




