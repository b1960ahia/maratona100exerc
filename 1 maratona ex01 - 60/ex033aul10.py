'''a = int(input('Digite o primeiro num: '))
b = int(input('Digite o segundo num: '))
c = int(input('Digite o terceiro num: '))
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior num e = {}'.format(maior))
print('O menor num e = {}'.format(menor))'''

# outra forma reduz comando

a = int(input('Digite o primeiro num: '))
b = int(input('Digite o segundo num: '))
c = int(input('Digite o terceiro num: '))
menor = a
if c < b and c < a:
    menor = c
if b < c and b < a:
    menor = b

maior = a
if c > b and c > a:
    maior = c
if b > c and b > a:
    maior = b
print('O maior valor e ={}, e o menor valor e ={}'.format(maior, menor))


