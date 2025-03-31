'''from random import choice
n1 = str(input('nome do primeiro aluno: '))
n2 = str(input('nome do segundo aluno: '))
n3 = str(input('nome do terceiro aluno: '))
n4 = str(input('nome do quarto aluno: '))
n5 = str(input('nome do quinto aluno: '))
lista = (n1, n2, n3, n4, n5)
escolhido = choice(lista)
print('O nome escolhido e {}'.format(escolhido))'''
import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
n5 = str(input('Quinto aluno: '))
lista = [n1, n2, n3, n4, n5]
escolhido = random.choice(lista)
print('O nome escolhido e {}'.format(escolhido))
