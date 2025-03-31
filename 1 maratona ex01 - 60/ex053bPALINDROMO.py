'''frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1 ):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não temos palindromo')'''


frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não temos palindromo')