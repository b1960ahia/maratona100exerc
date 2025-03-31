num1 = int(input('O primeiro numero e: '))
num2 = int(input('O segundo numero e: '))
if num1 > num2:
    print(' \033[35;40m O PRIMEIRO valor e MAIOR\033[m')
elif num2 > num1:
    print('\033[36;40m O SEGUNDO valor e MAIOR\033[m')
else:
    print('\033[34;40m Os dois são IGUAIS\033[m')
