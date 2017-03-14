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

pygame.event.get()

middleclick = False
rightclick = False
leftclick = False

mtimer = 0
rtimer = 0
ltimer = 0

deltatime = 0.0
lastTick = 0.0

while 1:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    timer = pygame.time.get_ticks()
    deltatime = (timer - lastTick)
    lastTick = timer

    grid.drawgraph()

    if pygame.mouse.get_pressed()[1] and middleclick == False:
        middleclick = True
        for node in grid.nodes:    
            x, y = pygame.mouse.get_pos()
            if x > node.nodevisual.visual.drawposition[0] and x < node.nodevisual.visual.drawposition[0] + 25:
                if y > node.nodevisual.visual.drawposition[1] and y < node.nodevisual.visual.drawposition[1] + 25:
                    node.clicked("wall")
                    info.drawinformation(node)
    if pygame.mouse.get_pressed()[0] and rightclick == False:
        rightclick = True
        for node in grid.nodes:    
            x, y = pygame.mouse.get_pos()
            if x > node.nodevisual.visual.drawposition[0] and x < node.nodevisual.visual.drawposition[0] + 25:
                if y > node.nodevisual.visual.drawposition[1] and y < node.nodevisual.visual.drawposition[1] + 25:
                    node.clicked("start")
                    info.drawinformation(node)
    if pygame.mouse.get_pressed()[2] and leftclick == False:
        leftclick = True
        for node in grid.nodes:    
            x, y = pygame.mouse.get_pos()
            if x > node.nodevisual.visual.drawposition[0] and x < node.nodevisual.visual.drawposition[0] + 25:
                if y > node.nodevisual.visual.drawposition[1] and y < node.nodevisual.visual.drawposition[1] + 25:                
                    node.clicked("goal")
                    info.drawinformation(node)

    if rightclick == True:
        rtimer = rtimer + (deltatime)
        if rtimer > 400:
            rtimer = 0
            rightclick = False
    
    if middleclick == True:
        mtimer = mtimer + (deltatime)
        if mtimer > 400:
            mtimer = 0
            middleclick = False
    
    if leftclick == True:
        ltimer = ltimer + (deltatime)
        if ltimer > 400:
            ltimer = 0
            leftclick = False



    pygame.display.flip()
    pygame.display.flip()


