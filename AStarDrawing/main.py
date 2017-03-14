''''''
from Utils import *
from Grid import *
import sys
import math

pygame.init()

grid = Graph(53, 25)

algorithm = AStar(grid)

grid.setupgraph()

info = NodeInformation([0, 750])
info.drawinformation(grid.nodes[0])

pygame.event.get()


while 1:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    grid.drawgraph()

    algorithm.enviormentupdate()
    algorithm.algorithmstep()

    grid.nodes[20].drawconnection(grid.nodes[21])

    pygame.display.flip()
    pygame.display.flip()


