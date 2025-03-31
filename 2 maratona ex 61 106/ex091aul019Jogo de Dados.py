from random import randint
from time import sleep
from  operator import itemgetter
dado = {'Joao': randint(1, 6),
        'Marco': randint(1, 6),
        'Paulo': randint(1, 6),
        'Roberto': randint(1, 6)}
ranking = []
print(' ===Valores sorteados:===  ')
for k, v in dado.items():
        print(f'  - {k} tirou {v} no dado.')
        sleep(2)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('  ====RANKING DOS JOGADORES====  ')
for i, v in enumerate(ranking):
        print(f'  {i + 1}º lugar: {v[0]} com {v[1]}.')
