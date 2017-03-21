'''main'''
import sys
import pygame
from Grid import AStar
from Grid import Graph
from Node import NodeInformation
from Game import GameLoop
from Game import AStarInteraction

GRID = Graph(53, 25)

ALGORITHM = AStar(GRID)

GRID.setupgraph()

INFO = NodeInformation([0, 750])

pygame.event.get()

GAMELOOP = GameLoop()

INTERACTION = AStarInteraction(ALGORITHM, GAMELOOP)
INTERACTION.addalgorithmstate("InfoMode", False)
INTERACTION.addalgorithmstate("UserStep", False)
INTERACTION.addbuttoncontrol("I", False)
INTERACTION.addbuttoncontrol("LeftMouse", False)
INTERACTION.addbuttoncontrol("MiddleMouse", False)
INTERACTION.addbuttoncontrol("RightMouse", False)

while GAMELOOP.update():    
    INTERACTION.algorithm.graph.drawgraph()
    INTERACTION.update()

    if ALGORITHM.current != None:
        INFO.drawinformation(ALGORITHM.current)



