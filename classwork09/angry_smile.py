import pygame
from pygame.draw import *
YELLOW = (225, 225, 0)
RED = (255,0,0)
BLACK =(0,0,0)
pygame.init()
MOUTH=(330, 450, 300, 50)
RESOLUTION=600
size=1000
FPS = 30
screen = pygame.display.set_mode((960, 720))
circle(screen, YELLOW, (480, 400), 200) # golova
circle(screen, RED, (400, 350), 40) #левый глаз
circle(screen, RED, (560, 360), 30) #правый глаз
circle(screen, BLACK, (400, 350), 20) # зрачок левый глаз
circle(screen, BLACK, (560, 360), 15) # зрачок правый глаз
rect(screen,BLACK, MOUTH) # рот
line(screen,BLACK,(360,270),(480,330), width=25)# левая бровь

pygame.display.update()
clock = pygame.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()