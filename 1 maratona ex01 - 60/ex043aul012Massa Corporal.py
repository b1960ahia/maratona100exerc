p = float(input('Qual e o seu peso? (kg)'))
a = float(input('Qual e a sua altura? (m)'))
imc = p / ( a ** 2 )
print('O IMC dessa pessoa é de \033[31;1;40m{:.1f}\033[m'.format(imc))
if imc < 18.5:
    print('\033[31;1;40;7m Abaixo do peso \033[m')
elif 18.5 <= imc < 25:
    print('\033[31;1;40;7m Peso ideal\033[m')
elif 25 <= imc < 30:
    print('\033[31;1;40;7m Vc esta com SOBREPESO\033[m')
elif 30 <= imc < 40:
    print('\033[31;1;40;7m Vc tem OBESIDADE\033[m')
else:
    print('\033[31;1;40;7m Vc tem OBESIDADE MORBIDA\033[m')

