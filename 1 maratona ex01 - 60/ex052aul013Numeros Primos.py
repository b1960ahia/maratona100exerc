num = int(input('Mostre um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print(end=' ')
        tot += 1
    else:
        print(end=' ')
    print('{}'.format(c), end=' ')
print('\nO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('O numero {} e primo'.format(num))
else:
    print('O numero {} nao e primo'.format(num))


