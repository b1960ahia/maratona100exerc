def area(c, l):
    a = c * l
    print(f'A area do terreno com  {c}m x {l}m = {c * l}m²')


print('  Controle de Terreno  ')
print('<>'* 20)
c = float(input('Largura (m):'))
l = float(input('Comprimento (m):'))
area(c, l)