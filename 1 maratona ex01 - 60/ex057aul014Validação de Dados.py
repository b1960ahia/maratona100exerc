sexo = str(input('Digite o sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor digite novamente: ')).strip().upper()[0]
print('Sexo {} informado com sucesso'.format(sexo))



