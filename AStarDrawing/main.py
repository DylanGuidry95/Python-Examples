''''''
from Utils import *
from Grid import *
import sys
import math

pygame.init()

grid = Graph(53, 25)

grid.setupgraph()

info = NodeInformation([0, 750])
info.drawinformation(grid.nodes[0])


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    grid.drawgraph()

    
    for node in grid.nodes:
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            if x > node.position[0] and x < node.position[0] + 25:
                if y > node.position[1] and y < node.position[1] + 25:
                    node.clicked()
                    print x, y


    pygame.display.flip()
    pygame.display.flip()


