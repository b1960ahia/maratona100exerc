print('{:=^40}'.format('  LOJAS J.PAULINO  '))
produto = float(input('Qual o valor do produto?: '))
opcao1 = produto - (produto * 10 / 100)
if opcao1:
#if produto - (produto * 10 / 100 ):
    print('Opção 1 = Pagamento a vista 10% de DESCONTO. Valor a pagar R${}'.format(opcao1))
opcao2 = produto - (produto * 5 / 100)
if opcao2:
#if produto - (produto * 5 / 100):
    print('Opção 2 = Pagamento cartao debito 5% de DESCONTO. Valor a pagar R${}'.format(opcao2))
opcao3 = produto / 2
if opcao3:
#if produto / 2:
    print('Opção 3 = Pagamento no cartao credito em 2 X R${} SEM JUROS'.format(opcao3))
opcao4 = ((produto * (20 / 100)) + produto) / 3
if opcao4:
#if ((produto * (20 / 100)) + produto) / 3:
    print('opção 4 = Pagamento no cartao de credito em 3 X de R${} Com 20% de JUROS'.format(opcao4))
if produto > 2000.00:
    print('Fale com GERENTE. Existem outros parcelamentos '.format(produto))







