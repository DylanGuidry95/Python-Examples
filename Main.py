import pygame
import sys
from Astar import Astar


pygame.init()
size = width, height = 1600, 900
screen = pygame.display.set_mode(size)



grid = Grid(10, 10)
grid.DrawGrid()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
    pygame.display.flip()