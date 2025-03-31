'''maiorpeso = 0
menorpeso = 0
for p in range(1, 6):
    peso = float(input('Informe o peso {}ª pessoa: '.format(p)))
    if p == 1:
        maiorpeso = peso
        menorpeso =peso
    else:
        if maiorpeso < peso:
            maiorpeso = peso
        if menorpeso > peso:
            menorpeso = peso
print('O maior peso e {}'.format(maiorpeso))
print('O menor peso e {}'.format(menorpeso))'''


print('=='*20)
print('{:<^40}'.format(' PESCADO DO FURIMBA '))
print('=='*20)
peso = preco = 0
total = peso * preco
pescado = ''
tipo = str(input('Qual tipo de pescado?: '))
peso = float(input('Qual o peso do pescado? [kg] : '))
preco = float(input('Qual o preço do pescado?: R$ '))
print('\033[35;1;40mO valor R$ {} x {}kg = Preço final R$ {:.2f} \033[m'.format(preco, peso, peso*preco))
print('{:<^40}'.format(' VOLTE SEMPRE '))









