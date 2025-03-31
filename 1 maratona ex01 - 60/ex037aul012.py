num = int(input('Digite um numero: '))
print('''Escolha uma das opções para conversão:
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    #print('{} em binario e {}'.format(num, bin(num)[2:]))
    print('O numero {} em binario e {}'.format(num, bin(num)))
elif opção == 2:
    #print('{} em octal e {}'.format(num, oct(num)[2:]))
    print('O numero {} em octal e {}'.format(num, oct(num)))
elif opção == 3:
    #print('{} em hexadecimal e {}'.format(num, hex(num)[2:]))
    print('O numero {} em hexadecimal e {}'.format(num, hex(num)))
else:
    print('\033[31;40;1m Opção invalida. Tente novamente!\033[m')
