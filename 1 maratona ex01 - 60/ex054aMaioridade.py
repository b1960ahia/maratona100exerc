from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    #nasc = int(input('Digite o ano de nascimento: '))#
    nasc = int(input('Em que ano a {}ª pessoa nasceu:'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} pessoas menores'.format(totmenor))
print('Temos {} pessoas maiores'.format(totmaior))

