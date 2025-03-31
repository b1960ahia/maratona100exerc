a = input('\033[34m Digite algo :')
print('O tipo primitivo desse valor é?', type(a))
print('É um número?', a.isnumeric())
print('Só tem espaços?', a.isspace())
print('É alfanumerico?', a.isalnum())
print('É alfabetico?', a.isalpha())
print('Esta em maiuscula?', a.isupper())
print('Ésta em minuscula?', a.islower())
print('Esta capitalizado?', a.istitle())


