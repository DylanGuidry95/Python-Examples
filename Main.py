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

    for node in grid.nodes:
        grid.nodes[node].DrawNode((255, 255, 255))
    
    grid.nodes[algorithm.start].DrawNode((0, 255, 0))
    grid.nodes[algorithm.goal].DrawNode((0, 0, 255))

    pygame.display.flip()
    pygame.display.flip()

