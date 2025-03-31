'''num = int(input('Digite um numero: '))
impar = num % 2
if impar:
    print('O numero sera {}'.format(impar))
else:
    print('O numero e par')'''
num = int(input('Digite um numero qualquer: '))
impar = num % 2
if impar == 0:
    print('O numero {} e par'.format(num))
else:
    print('O numero {} e impar'.format(num))


