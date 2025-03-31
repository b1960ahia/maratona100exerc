resp = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
media = 0
while resp in 'Ss':
    n = int(input('Digite um numero 🙏: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print('Voce digitou {} numeros e a media foi {}'.format(cont, media))
print('O maior numero é {} e o menor é {}'.format(maior, menor))
print('Trabalho finalizado 👊🤩:')


