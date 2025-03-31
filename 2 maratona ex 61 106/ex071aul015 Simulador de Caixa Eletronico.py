print('=~'*9)
print('{:^9}'.format(' BANCO JB INVEST'))
print('=~'*9)
valor = int(input('Qual valor vc quer sacar: R$ '))
total = valor
cedatual = 50
totced = 0
while True:
    if total >= cedatual:
        total -= cedatual
        totced += 1
    else:
        print(f'Total de {totced} cedulas de R$ {cedatual} ')
        if cedatual == 50:
            cedatual = 20
        elif cedatual == 20:
            cedatual = 10
        elif cedatual == 10:
            cedatual = 1
        totced = 0
        if total == 0:
            break
print('{:=^40}'.format('SAQUE CONCLUIDO COM SUCESSO'))




