'''import pygame
pygame.init()
pygame.mixer.music.load (ex021.mp3)
pygame.mixer.music.play()
pygame.event.wait()'''

computador = randint (0, 7)
print('Pensarei um numero entre 0 e 7, tente advinhar...')
jogador = int(input('Em que numero eu pensei?'))
print('processando...')
sleep(2)
if jogador == computador:
    print('Parabens vc me venceu')
else:
    print('Ganhei! Pensei no numero {} e nao no {}'.format(computador, jogador))