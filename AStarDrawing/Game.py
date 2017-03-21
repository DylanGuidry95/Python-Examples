'''Modules that control the main game loop'''
#pylint: disable=E1101
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
        '''Defines new controls for the user'''
        if not self.buttons.has_key(buttonname):
            self.buttons[buttonname] = state
            self.timers[buttonname] = 0.0

    def addalgorithmstate(self, statename, state):
        '''Defines new states for the aplpication to be in'''
        self.states[statename] = state

    def update(self):
        '''called every tick'''
        self.buttonpressdelay()
        userinput = self.getbuttonpressed()
        clickednode = self.getnodeclicked()
        if userinput == "ToggleInfoMode":
            self.infomode(clickednode)
        if clickednode != None:
            self.changeenviorment(clickednode, userinput)

    def buttonpressdelay(self):
        '''Delays the time betwen key input checks by the system'''
        for iterator in range(0, len(self.buttons)):
            if self.buttons.items()[iterator]:
                self.timers[iterator] = self.timers[iterator] + self.gameloop.deltatime
                if self.timers[iterator] > 400:
                    self.timers[iterator] = 0
                    self.buttons[iterator] = False

    def infomode(self, node):
        '''Disables the ability to modify the area but gives certain inforamtion about
        the node that was clicked'''
        state = self.states.get("InfoMode", None)
        if state != None:
            self.states["InfoMode"] = not self.states["InfoMode"]
            state = self.states.get("InfoMode", None)
        if state:
            self.algorithm.nodeinfo.drawinformation(node)

    def changeenviorment(self, node, action):
        '''Modifies the play area by allowing the user to set start node, goal node, and
        walls'''
        state = self.states.get("InfoMode", None)
        if not state:
            if action == "SetStart":
                self.algorithm.setstartnode(node)
            elif action == "SetWall":
                self.algorithm.modifywall(node)
            elif action == "SetGoal":
                self.algorithm.setgoalnode(node)

    def getbuttonpressed(self):
        '''Checks to see what button pressed and returns a string value to represent
        the control that user used'''
        keys = pygame.key.get_pressed()
        buttons = pygame.mouse.get_pressed()
        if keys[pygame.K_i] and not self.buttons["I"]:
            self.buttons["I"] = True
            return "ToggleInfoMode"
        elif buttons[0] and not self.buttons["LeftMouse"]:
            self.buttons["LeftMouse"] = True
            return "SetStart"
        elif buttons[1] and not self.buttons["MiddleMouse"]:
            self.buttons["MiddleMouse"] = True
            return "SetWall"
        elif buttons[2] and not self.buttons["RightMouse"]:
            self.buttons["RightMouse"] = True
            return "SetGoal"

    def getnodeclicked(self):
        '''If the mouse cursur is at the same positon as node returns that node'''
        for node in self.algorithm.graph.nodes:
            mxpos, mypos = pygame.mouse.get_pos()
            if node.visual.collisioncheck([mxpos, mypos]):
                return node
        return None
