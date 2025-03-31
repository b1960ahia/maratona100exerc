n= int(input('\033[50;1m digite um numero: \033[m'))
d= n * 2
t= n * 3
r= n ** (1/2)
print('\033[40;1m analizando numero {}\033[m, seu dobro e {}\nseu triplo e {}\nsua raiz e {:.1f}\n' .format(n, d, t, r))
