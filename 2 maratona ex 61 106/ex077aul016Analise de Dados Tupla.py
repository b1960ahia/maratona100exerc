palavra = ('poeira','cadeira','pandeiro',
           'caju','mesa','casado','viuvo')
for p in palavra:
    print(f'\nNa palavra \033[34;1m{p.upper()}\033[m temos as vogais:', end=' ')
    for vog in p:
        if vog.lower() in 'aeiou':
            print(vog, end=',')






