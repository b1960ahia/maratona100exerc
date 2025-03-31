tot18M = 0
totHom = 0
totM20 = 0
while True:
    idade = int(input('Qual sua idade? :'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F]:')).strip().upper()[0]
    if idade >= 18:
        tot18M += 1
    if sexo == 'M':
        totHom += 1
    elif sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Fim de consulta')
print(f'Total pessoas mais de 18 anos {tot18M}')
print(f'Foi cadastrado {totHom} homem(s)')
print(f'Cadstrou-se {totM20} mulher(s) com menos de 20 anos')





