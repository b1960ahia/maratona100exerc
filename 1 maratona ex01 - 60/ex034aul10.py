salario = float(input('Qual o seu salario atual?: R$ '))
a = salario + (salario * 10 / 100)
b = salario + (salario * 15 / 100)
if salario >= 1250.00:
    print('\033[31;1m O novo salario e R$ {}\033[m'.format(a))
else:
    print('\033[35;1m O novo salario e R$ {}\033[m'.format(b))
