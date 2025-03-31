print('='*30)
print('{:<^30}'.format('Lista de Preços'))
print('='*30)
produtos = ('cenoura', 5.00,
            'alface', 2.00,
            'tomate', 4.50,
            'batata', 5.00,
            'pepino', 3.50,
            'cebola',4.70,
            'inhame',6.30,
            'laranja',5.50,
            'abacaxi',46.80)
for itens in range(0, len(produtos)):
    if itens % 2 == 0:
        print(f'{produtos[itens]:.<20}',end='')
    else:
        print(f'R$...{produtos[itens]:>5.2f}')
print('<<<<<<<<<Volte Sempre<<<<<<<<<')



