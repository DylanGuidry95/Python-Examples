''''''
from Utils import *
import sys

size = width, height = 1600, 900
screen = pygame.display.set_mode(size)

pygame.init()

text = Text(screen, [100,100], [WHITE, BLACK], "Dick Butt", 15)

text.draw()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
    pygame.display.flip()


