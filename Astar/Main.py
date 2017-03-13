import sys
from AStar import *
import pygame
from Grid import Grid
import random

pygame.init()

grid = Grid(10, 10)
startIndex = random.randint(0,len(grid.nodes))
goalIndex = random.randint(0,len(grid.nodes))
algorithm = AStar(grid, grid.nodes.keys()[startIndex], grid.nodes.keys()[goalIndex])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    algorithm.Step()

    pygame.display.flip()
    pygame.display.flip()

