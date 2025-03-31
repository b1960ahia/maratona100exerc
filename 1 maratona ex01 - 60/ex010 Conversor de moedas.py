r = float(input('\033[30m Quanto dinheiro vc tem :'))
d = r / 3.27
print('Com \033[35;1mR${} \033[36mvc pode comprar \033[35;7m${:.1f}\033[m'.format(r, d))
