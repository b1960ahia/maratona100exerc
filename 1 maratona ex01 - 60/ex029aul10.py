'''vcarro = float(input('Qual e a velocidade do carro?'))
if vcarro > 80:
    print('Carro multado ')
    multa = (vcarro - 80) * 7
    print('Vc vai pagar uma multa de R$ {:.1f}'.format(multa))
print('Bom dia! Dirija com segurança')'''
vcarro = float(input('Qual a velocidade atual? :'))
multa = (vcarro - 80) * 7
if vcarro > 80:
    print('\033[31mMULTADO. Excedeu a velocidade de 80km/h. Multa de R${:.1f}\033[m'.format(multa))
print('Bom dia! Dirija com cuidado.')





