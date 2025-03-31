mediaidade = 0
somaidade = 0
maisvelho = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('======={}ª PESSOA======='.format(p))
    nome = str(input('Nome : ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maisvelho = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        totmulher20 += 1
        mediaidade = somaidade / 4
print('Tem {} mulheres c/menos de 20 anos'.format(totmulher20))
print('O nome mais velho e {} e tem {} anos'.format(nome, maisvelho))
print('A media de idade e {} anos '.format(mediaidade))
