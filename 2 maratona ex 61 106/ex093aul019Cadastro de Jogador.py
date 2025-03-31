
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(0, part):
    partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('<>'*20)
print(jogador)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print(f'\033[40mO jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.\033[m')
for i, v in enumerate(jogador['gols']):
    print(f'  ===Na {i+1}ª partida {jogador["nome"]} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols.')