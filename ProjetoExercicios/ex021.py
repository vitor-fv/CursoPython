import pygame
# Iniciando o pygame
pygame.init()
# Importando música
pygame.mixer.music.load('arquivos/ex021.mp3')
# Dar o play na música
pygame.mixer.music.play()
# Após att do pygame necessita o uso do input
input()
# Finalizar música
pygame.event.wait()
