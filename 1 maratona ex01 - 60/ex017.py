'''co = float(input('Medida do cateto oposto: '))
ca = float(input('Medida do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print('A medida da hipotenusa e {:.2f}'.format(hi))'''
import math
co = float(input('Cateto oposto: '))
ca = float(input('catetto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa e = {:.2f}'.format(hi))


