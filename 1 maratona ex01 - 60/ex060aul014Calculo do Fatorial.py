'''from math import factorial
n = int(input(' Digite o numero e calcule o factorial: '))
f = factorial(n)
print('O factorial de {} e {}'.format( n, f))'''

n = int(input('Digite um numero e calcule factorial:'))
c = n
f = 1
print('{}! = '.format(n),end='')
while c != 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ',end='')
    else:
        print(' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))


