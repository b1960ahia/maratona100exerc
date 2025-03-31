def leiaInt(msg):
    ok = False
    v = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero valido.')
        if ok:
            break
    return v


#programa principal
n =leiaInt('Digite um numero:')
#n = int(input('Digite um numero:'))
print(f'Vc digitou o numero {n} ')