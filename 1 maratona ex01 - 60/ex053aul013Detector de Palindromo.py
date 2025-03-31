frase = str(input('digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
#inverso = ''
inverso = junto[::-1] # inseriu essa linha e tirou o for (fatiamento)
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('E um PALINDROMO')
else:
    print('Nao e um PALINDROMO')





