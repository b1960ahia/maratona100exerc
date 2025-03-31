ficha = []
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota1: '))
    nota2 = float(input('nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?: [S/N]'))
    if resp in 'Nn':
        break
print(ficha)
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('>'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('>-'*20)
    opc = int(input('Mostrar nota do aluno [999 para]: '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('###### Volte Sempre######')


