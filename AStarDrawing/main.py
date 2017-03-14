
'''main'''
import sys
import pygame
from Grid import AStar
from Grid import Graph
from Node import NodeInformation


pygame.init()

GRID = Graph(53, 25)

ALGORITHM = AStar(GRID)

GRID.setupgraph()

INFO = NodeInformation([0, 750])

pygame.event.get()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    GRID.drawgraph()

    ALGORITHM.enviormentupdate()
    ALGORITHM.algorithmstep()

    if ALGORITHM.current != None:
        INFO.drawinformation(ALGORITHM.current)

    pygame.display.flip()
    pygame.display.flip()


