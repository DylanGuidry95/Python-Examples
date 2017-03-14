'''All information for nodes and how they are displayed'''
import pygame
from Utils import Rectangle
from Utils import Circle
from Utils import Line
from Utils import Text
from Utils import WHITE
from Utils import BLACK
from Utils import GREEN
from Utils import BLUE
from Utils import RED
from Utils import YELLOW

SIZE = WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode(SIZE)

class NodeObject(object):
    '''Visual representation of the node on the screen'''
    def __init__(self, position, color):
        self.position = position
        self.visual = Rectangle(SCREEN, [position[0], position[1]], color, [25, 25], 30)

    def drawnode(self):
        '''Draws the node to the screen'''
        self.visual.draw()

    def changecolor(self, color):
        '''Changes the color of the object on the screen'''
        self.visual.changecolor(color)

    def drawtonode(self, node):
        '''Draws a line from the node to its parent node'''
        if node != None:
            circle = Circle(SCREEN, [self.drawposition()[0] + (25/2),
                                     self.drawposition()[1] + (25/2)],
                            BLACK, 10)
            line = Line(SCREEN, [[self.drawposition()[0] + (25/2), self.drawposition()[1] + (25/2)],
                                 [node.visual.drawposition()[0] + (25/2),
                                  node.visual.drawposition()[1] + (25/2)]], BLACK, 2)
            circle.draw()
            line.draw()

    def drawposition(self):
        '''gets the position of the object in screen space'''
        return self.visual.drawposition

    def collisioncheck(self, colpos):
        '''Checks to see if collpos is inside of the objects draw space'''
        if colpos[0] > self.drawposition()[0] and colpos[0] < self.drawposition()[0] + 25:
            if colpos[1] > self.drawposition()[1] and colpos[1] < self.drawposition()[1] + 25:
                return True
        else:
            return False

class Node(object):
    '''A node object to be used in the Astar algorithm'''
    def __init__(self, position):
        self.position = position
        self.visual = NodeObject(self.position, WHITE)
        self.parent = None
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.iswall = False
        self.isgoal = False
        self.isstart = False

    def drawvisual(self):
        '''Invokes the drawnode funciton from visual'''
        self.visual.drawnode()

    def drawconnection(self, node):
        '''invokes the drawtonode function in visual component and gives it the node argument'''
        self.visual.drawtonode(node)

    def changestate(self, state):
        '''Changes the state of the node
        based on the value of state the node will change color and the
        value of various components of a node will change'''
        if state == "start" and not self.isgoal:
            self.isstart = not self.isstart
            if self.isstart:
                self.visual.changecolor(GREEN)
            else:
                state = "default"
        elif state == "goal"and not self.isstart:
            self.isgoal = not self.isgoal
            if self.isgoal:
                self.visual.changecolor(BLUE)
            else:
                state = "default"
        elif state == "wall"and not self.isgoal and not self.isstart:
            self.iswall = not self.iswall
            if self.iswall:
                self.visual.changecolor(RED)
            else:
                state = "default"
        if state == "default":
            self.iswall = False
            self.isstart = False
            self.isgoal = False
            self.visual.changecolor(WHITE)

    def getneighbors(self, graph):
        '''Gets all neighbors of the node in the graph passed in to function call'''
        neighbors = []

        left = [self.position[0] - 1, self.position[1]]
        topleft = [self.position[0] - 1, self.position[1] + 1]
        top = [self.position[0], self.position[1] + 1]
        topright = [self.position[0] + 1, self.position[1] + 1]
        right = [self.position[0] + 1, self.position[1]]
        bottomright = [self.position[0] + 1, self.position[1] - 1]
        bottom = [self.position[0], self.position[1] - 1]
        bottomleft = [self.position[0] - 1, self.position[1] - 1]
        neighborpositions = [left, topleft, top, topright, right, bottomright, bottom, bottomleft]

        for node in graph.nodes:
            for position in neighborpositions:
                if node.position[0] == position[0] and node.position[1] == position[1]:
                    neighbors.append(node)
                    node.visual.changecolor(YELLOW)
        return neighbors

    def calcgscore(self, node):
        '''Calculates the gscore of the current node based on the location of the node passed input
        if the current node doesnt have a parent the node passed in will become its parent
        if it does have a node a temp gscore will be calculated and if the new gscore is better
        than the current its new parent will be the node passed in'''
        if self.parent is None:
            if node.position[0] == self.position[0] or node.position[1] == self.position[1]:
                node.gscore = 10
            else:
                node.gscore = 14
            self.parent = node
        else:
            tempgscore = self.gscore
            if node.position[0] == self.position[0] or node.position[1] == self.position[1]:
                tempgscore = 10
            else:
                tempgscore = 14
            if tempgscore < self.gscore:
                self.parent = node
        self.visual.drawtonode(self.parent)

class NodeInformation(object):
    '''Creates text to display to the window with a nodes gscore, hscore, and fscore'''
    def __init__(self, position):
        self.position = position

    def drawinformation(self, node):
        '''Updates the text element with the information of the node passed in'''
        gposition = self.position
        hposition = [self.position[0], self.position[1] + 50]
        fposition = [self.position[0], self.position[1] + 100]
        gtext = Text(SCREEN, gposition, [WHITE, BLACK], "G Score: " + str(node.gscore), 25)
        htext = Text(SCREEN, hposition, [WHITE, BLACK], "H Score:" + str(node.hscore), 25)
        ftext = Text(SCREEN, fposition, [WHITE, BLACK], "F Score:" + str(node.fscore), 25)
        gtext.draw()
        htext.draw()
        ftext.draw()
