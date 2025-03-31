'''import math
angulo = float(input('digite um angulo: '))
seno = math.sin(math.radians(angulo))
print('o angulo {} tem seno {}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo {} tem cosseno {}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo {} tem tangente {}'.format(angulo, tangente))'''
from math import radians, sin, cos, tan

angulo = float(input('digite um angulo: '))
seno = sin(radians(angulo))
print('O angulo {} tem o seno {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('o angulo de {} tem cosseno {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('o angulo {} tem a tangente {:.2f}'.format(angulo, tangente))
