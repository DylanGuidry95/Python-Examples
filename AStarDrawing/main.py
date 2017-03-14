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

    grid.nodes[0].drawconnection(grid.nodes[26])

    for node in grid.nodes:
        if pygame.mouse.get_pressed()[1]:
            x, y = pygame.mouse.get_pos()
            if x > node.nodevisual.visual.drawposition[0] and x < node.nodevisual.visual.drawposition[0] + 25:
                if y > node.nodevisual.visual.drawposition[1] and y < node.nodevisual.visual.drawposition[1] + 25:
                    node.clicked()
                    info.drawinformation(node)


    pygame.display.flip()
    pygame.display.flip()


