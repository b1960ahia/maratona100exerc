nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome em maisculas é {}'.format(nome.upper()))
print('Seu nome em minuscula é {}'.format(nome.lower()))
print('Seu nome tem {} letras sem espaço'.format(len(nome) - nome.count(' ')))
print('seu nome tem {} letras com o espaço'.format(len(nome)))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
'''nome = 'João Paulino Bahia Filho'
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(len(nome))
print(nome.find(' '))'''


