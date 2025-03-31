from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(pess)))
    idade = atual - nasc
    if idade < 21:
     totmenor += 1
    else:
        totmaior += 1
print('Tivemos {} pessoas MENOR idade'.format(totmenor))
print('Tivemos {} pessoa MAIOR idade'.format(totmaior))

