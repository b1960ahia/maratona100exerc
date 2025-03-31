sa = float(input('O valor atual do salario é: R$'))
a = (sa * 15 / 100)
ns = sa + a
print('Novo salario com 15% de aumento é = (sa) R${} + (a) R${:.2f} = (ns) R${:.2f}'.format(sa, a, ns))
