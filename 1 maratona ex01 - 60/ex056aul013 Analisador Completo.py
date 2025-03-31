somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-------{}ªPessoa-------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade +=idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if idade < 20 and sexo in 'Ff':
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo e de {} anos'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos'.format(nomemaisvelho, maioridadehomem))
print('No grupo temos {} mulheres com menos de 20 anos'.format(totmulher20))



