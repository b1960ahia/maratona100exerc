l = float(input('Qual a largura da parede :'))
h = float(input('Qual a altura da parede :'))
a = l * h
print('A area da parede e {}mt x {}mt = {:.3}'.format(l, h, a))
tinta = a / 2
print('Para pintar a parede sera gasto {:.3}lt'.format(tinta))
