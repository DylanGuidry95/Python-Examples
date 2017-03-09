import sys
from AStar import *
import pygame
from Grid import Grid

pygame.init()

grid = Grid(10, 10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
    pygame.display.flip()