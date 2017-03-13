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
            p = pygame.mouse.get_pos()
            mousepos = (p[0], p[1])
            distance = math.sqrt((mousepos[0] - node.position[0]) +
                        (mousepos[1] - node.position[1]))
            if distance < 1:
                node.clicked()

    p = pygame.mouse.get_pos()
    mouse = Text(screen, [500, 775], [WHITE,BLACK], 
    str(p[0]) + "," + str(p[1]) , 25)
    mouse.draw()

    pygame.display.flip()
    pygame.display.flip()


