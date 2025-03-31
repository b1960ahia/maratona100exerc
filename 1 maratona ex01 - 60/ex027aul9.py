'''nome = str(input('Digite um nome:')).strip()
print('Muito prazer em te conhecer')
print('O seu nome tem {} caracteres'.format(len(nome.rstrip())))
print('O seu primeiro nome e {}'.format(nome[:5]))
print('O seu ultimo nome e {}'.format(nome[19:]))'''
n = str((input('Digite seu nome completo:'))).strip()
print('Muito prazer em te conhecer!')
nome = n.split()
print(nome)
print('O seu primeiro nome e: {} '.format(nome[0]))
print('O seu ultimo nome e: {}'.format(nome[len(nome)-1]))



