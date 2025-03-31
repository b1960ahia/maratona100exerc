frase = str(input('Escreva uma frase:')).strip().upper()
print('Quantas vezes aparece letra A? {}'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posiição {}'.format(frase.rfind('A')+1))
#O +1 colocado para adequar a posiçao na frase. Pode tirar e fica leitura do Python.
'''frase = str(input('Escreva uma frase:')).strip()
print('Quantas vezes aparece a letra A?{}'.format(frase.count('a')))
print('A primeira letra A aparece na posção {}'.format(frase.find('a')))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('a')))'''
