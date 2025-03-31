from datetime import date
atual = date.today().year
nome = str(input('Nome do atleta:🏋️'))
ano = int(input('digite o ano que nasceu: '))
#atual = int(input('Digite ano atual: '))
idade = atual - ano
print('\033[40;1mVc tem {} anos\033[m'.format(idade))
if idade <= 9:
    print('\033[31;1m Sua categoria é MIRIM 🧑‍🎄\033[m'.format(idade))
elif idade <= 14:
    print('\033[32;1m Sua categoria é INFANTIL 🚴🏿‍♀️\033[m'.format(idade))
elif idade <= 19:
    print('\033[33;1m Sua categoria é JUNIOR 🏄🏿\033[m'.format(idade))
elif idade <= 25:
    print('\033[34;1m Sua categoria é SENIOR 👨🏾‍⚖️ \033[m'.format(idade))
else:
    print('\033[35;1m Sua categoria é MASTER 👴🏾\033[m️')
