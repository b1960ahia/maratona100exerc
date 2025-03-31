s1 = float(input('Comprimento do primeiro segmento: '))
s2 = float(input('Comprimento do segundo segmento: '))
s3 = float(input('Comprimento do terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos acima podem formar triangulo.')
    #print('As medidas das retas r1 = {}  , r2 = {}  , r3 = {}  , formam triangulo.'.format(s1, s2, s3))
else:
    print('Náo formam triangulo')
