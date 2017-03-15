'''main'''
import sys
import pygame
from Grid import AStar
from Grid import Graph
from Node import NodeInformation
from Game import GameLoop


GRID = Graph(53, 25)

ALGORITHM = AStar(GRID)

GRID.setupgraph()

INFO = NodeInformation([0, 750])

pygame.event.get()

GAMELOOP = GameLoop()

while GAMELOOP.update():
    GRID.drawgraph()

    ALGORITHM.enviormentupdate(GAMELOOP.deltatime)
    ALGORITHM.algorithmstep()

    if ALGORITHM.current != None:
        INFO.drawinformation(ALGORITHM.current)



