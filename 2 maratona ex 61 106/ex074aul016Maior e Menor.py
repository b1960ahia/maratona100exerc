from random import randint
n = (randint(1, 25),randint(1, 25),randint(1, 25),randint(1, 25),
randint(1, 25),randint(1, 25),randint(1, 25),randint(1, 25),
randint(1, 25),randint(1, 25),randint(1, 25),randint(1, 25),
randint(1, 25),randint(1, 25),randint(1, 25))
#print(f'Eu sorteei os valores {n}') [L6 + L10 + L11]
print('\033[40;31mOs valores sorteados são:\033[m ')
for num in n:
    print(f'\033[35;1m{num}\033[m', end= ' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')