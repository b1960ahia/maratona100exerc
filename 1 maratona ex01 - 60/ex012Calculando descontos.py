prod = float(input('O preço da mercadoria é: R$'))
prom = prod * 5 / 100
np = prod - prom
print('O preço na promoção com 5% de desconto e = (valor) R${} - (desconto) R${} = (novo valor) R${:.2f}'.format(prod, prom, np))
