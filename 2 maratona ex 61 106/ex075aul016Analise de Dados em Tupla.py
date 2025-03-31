#Minha solução
n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
n3 = int(input('Digite o 3º numero: '))
n4 = int(input('Digite o 4º numero: '))
print(f'Vc digitou os valores {n1}, {n2}, {n3}, {n4}')
num = (3,8,9,10)
print(f'O 8 apareceu {num.count(8)} vezes')
print(f'O 10 apareceu na posição {num.index(10)}')
print('Os pares digitados foram: ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=',')


'''num = (int(input('Digite 1º numero: ')),
    int(input('Digite 2º numero: ')),
    int(input('Digite 3º numero: ')),
    int(input('Digite 4º numero: ')))
print(f'Vc digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na posição: {num.index(3)}')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=',')'''