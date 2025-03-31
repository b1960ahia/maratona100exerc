vcasa = float(input('\033[33;1m Qual o valor da casa?:R$ '))
salario = float(input('\033[33;1m''Qual o salario?:R$ '))
anos = int(input('\033[33;1m Quantos anos?: \033[m'))
prazo = 7 * 12
mensal = vcasa / prazo
print('valor da prestação = {:.2f} / {} = \033[34;1m {:.2f}'.format(vcasa, prazo, mensal))
print('Prazo = {}meses'.format(prazo))
if vcasa / prazo >= salario * 30/100:
    print('\033[31;1;4m Emprestimo negado')
else:
    print('\033[32;1;4m Emprestimo aprovado')

