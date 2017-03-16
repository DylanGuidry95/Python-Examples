'''Modules that control the main game loop'''
import sys
import pygame

class GameLoop(object):
    '''Controls the game loop and calcualtes delta time for the application'''
    def __init__(self):
        self.deltatime = 0.0
        self.lasttick = 0.0
        pygame.init()

    def update(self):
        '''Handles the execution of the application'''
        self.calcdeltatime()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return False

        pygame.display.flip()
        pygame.display.flip()
        return True

    def calcdeltatime(self):
        '''Calculates the delta time for the application'''
        timer = pygame.time.get_ticks()
        self.deltatime = (timer - self.lasttick)
        self.lasttick = timer

class AStarInteraction(object):
    '''Handles all of the user interaction with the astar algorithm'''
    def __init__(self, algorithm, gameloop):
        self.gameloop = gameloop
        self.algorithm = algorithm
        self.states = {}
        self.buttons = {}
        self.timers = {}

    def addbuttoncontrol(self, buttonname, state):
        if not self.buttons.has_key(buttonname):
            self.buttons[buttonname] = state
            self.timers[buttonname] = 0.0

    def addalgorithmstate(self,statename, state):
        self.states[statename] = state

    def update(self, deltatime):
        userinput = self.getbuttonpressed()
        clickednode = self.getnodeclicked()
        if userinput == "ToggleInfoMode":
            self.infomode(clickednode)
        if clickednode != None:
            self.infomode(clickednode)
            self.changeenviorment(clickednode, userinput)


    def buttonpressdelay(self):
        for iterator in range(0, len(self.buttons)):
            if self.buttons[iterator]:
                self.timers[iterator] = self.timers[iterator] + self.gameloop.deltatime
                if self.timers[iterator] > 400:
                    self.timers[iterator] = 0
                    self.buttons[iterator] = False


    def infomode(self, node):
        state = self.states.get("InfoMode", None)
        if state != None:
            self.states["InfoMode"] = not self.states["InfoMode"]
        if state:
            self.algorithm.nodeinfo.drawinformation(node)

    def changeenviorment(self, node, action):
        state = self.states.get("InfoMode", None)
        if not state:
            if action == "SetStart":
                self.algorithm.setstartnode(node)
            elif action == "SetWall":
                self.algorithm.modifywall(node)
            elif action == "SetGoal":
                self.algorithm.setgoalnode(node)


    def getbuttonpressed(self):
        keys = pygame.key.get_pressed()
        buttons = pygame.mouse.get_pressed()
        if keys[pygame.K_i]:
            self.buttons["I"] = True
            return "ToggleInfoMode"
        elif buttons[0]:
            self.buttons["LeftMouse"] = True
            return "SetStart"
        elif buttons[1]:
            self.buttons["MiddleMouse"] = True
            return "SetWall"
        elif buttons[2]:
            self.buttons["RightMouse"] = True
            return "SetGoal"

    def getnodeclicked(self):
        for node in self.algorithm.graph.nodes:
            mxpos, mypos = pygame.mouse.get_pos()
            if node.visual.collisioncheck([mxpos, mypos]):
                return node
        return None
