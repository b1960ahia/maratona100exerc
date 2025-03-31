n1 = float(input('Digite primeira nota: '))
n2 = float(input('Digite segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {}'.format(m))
if m < 5:
    print('\033[31;40;1m Vc foi REPROVADO!\033[m')
elif m >= 5 and m < 7:
#elif 5 <= m < 7:
    print('\033[33;40;1m Vc ficou em RECUPERAÇÃO!\033[m')
else:
    print('\033[32;40;1m Sorria! Vc foi APROVADO!\033[m')

