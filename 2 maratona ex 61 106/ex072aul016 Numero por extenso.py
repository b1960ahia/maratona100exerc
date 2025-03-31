cont = ('zero','um','dois','tres','quatro','cinco',
        'seis','sete','oito','nove','dez',
        'onze','doze','treze','catorze','quinze',
        'dezesseis','dezssete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Quer continuar...', end='')
print(f'O numero digitado é o {cont[num]}')
