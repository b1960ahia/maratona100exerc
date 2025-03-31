#from datetime import date
#atual = date.today().year
ano = int(input('Informe ano de nascimento: '))
anoatual = int(input('digite ano atual: '))
idatual = anoatual - ano
print('Vc nasceu no ano {} fez \033[40;1m {} anos em {}.\033[m'.format(ano,idatual, anoatual))
if idatual == 18:
    print('\033[31;1mChegou a hora de se alistar.\033[m')
elif idatual < 18:
    saldo = 18 - idatual
    print('\033[40;1;7m Ainda nao esta na hora de se alistar. \033[31;1m Faltam {} anos.\033[m'.format(saldo))
    ano = saldo + anoatual
    print('Seu alistamento sera em {}'.format(ano))
elif idatual > 18:
    saldo = idatual - 18
    print('Passou do tempo de se alistar. Ja se passaram {} anos. '.format(saldo))
    ano = anoatual - saldo
    print('\033[40;1;7mVc deveria ter se alistado em {}\033[m'.format(ano))



