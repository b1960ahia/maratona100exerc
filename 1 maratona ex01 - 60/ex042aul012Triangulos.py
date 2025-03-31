l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    #print('Os seguimentos {}, {} e {} \033[32;1m podem formar TRIANGULO\033[m'.format(l1, l2, l3))
    print('Os seguimentos acima \033[40;1m podem formar TRIANGULO\033[m ', end='')
if l1 == l2 == l3:
    print('\033[45;1;30m EQUILATERO\033[m')
    #print('As medidas {}, {} e {}, formam \033[35;1m triangulo EQUILATERO\033[m'.format(l1,l2,l3))
elif l1 == l2 and l1 != l3 and l2 != l3:
    print('\033[46;1;30m ISOSCELES\033[m')
#if l1 == l2 and l1 != l3 and l2 != l3:
    #print('As medidas {}, {} e {}, formam \033[36;1m triangulo ISOSCELES\033[m'.format(l1, l2, l3))
elif l1 != l2 != l3 != l1:
    print('\033[44;1;30m ESCALENO\033[m')
else:
    print('\033[41;30;1m NAO FORMAM TRIANGULO\033[m')
#if l1 != l2 != l3 != l1:
    #print('As medidas {}, {} e {} formam \033[40;1m triangulo ESCALENO\033[m'.format(l1, l2, l3))
#else:
    #print('\033[41;1;40m NÃO FORMAM TRIANGULO\033[m')