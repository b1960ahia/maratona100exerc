'''cont = 0
soma = 0
while True:
    n = int(input('Digite um numero? [999 parar] :'))
    print('='* 20)
    if n == 999:
        break
    cont += 1
    soma += n
print(f'\033[36;1;41m A soma è {soma} e vc digitou {cont} numeros.\033[m')'''

cont = 0
soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} numeros e a soma foi {soma}')

