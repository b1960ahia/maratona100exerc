'''ano = int(input('Digite um ano: '))
bisexto = ano % 4
if bisexto == 0:
    print('O ano {} e bisexto'.format(ano))
else:
    print('O ano {} nao e bisexto'.format(ano))'''
'''ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 or ano % 400 ==0:
    print('O ano {} e bisexto'.format(ano))
else:
    print('O ano {} nao e bisexto'.format(ano))'''
from datetime import date
ano = int(input('Digite um ano (Coloque zero analisar ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
    print('\033[31m O ano {} e bisexto\033[m'.format(ano))
else:
    print('\033[36m O ano {} nao e bisexto\033[m'.format(ano))

