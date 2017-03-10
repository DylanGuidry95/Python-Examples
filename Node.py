import pygame


size = width, height = 1600, 900
screen = pygame.display.set_mode(size)

class NodeVisual(object):
    def __init__(self, xPos, yPos):
        self.width = 10
        self.height = 10
        self.margin = 10
        self.top = (self.margin + 10) * yPos + self.margin
        self.left = (self.margin + 10) * xPos + self.margin
        self.xPos = xPos
        self.yPos = yPos

    def DrawNode(self, color):
        pygame.draw.rect(screen, color, (self.left, self.top, self.width, self.height))

class Node(object):
    def __init__(self, xPos, yPos, value):
        self.xPos = xPos
        self.yPos = yPos
        self.value = value
        self.parent = None
        self.FScore = 0
        self.GScore = 0
        self.HScore = 0

    def SetFScore(self):
            return self.GScore + self.HScore

    def SetGScore(self):
        if self.parent is None:
            if self.parent.xPos == self.xPos or self.parent.yPos == self.yPos:
                self.GScore = 10
            else:
                self.GScore = 14
        else:
            tempG = 0
            if self.parent.xPos == self.xPos or self.parent.yPos == self.yPos:
                tempG = 10
            else:
                tempG = 14
            if tempG < self.GScore:
                GScore = tempG

    def SetHScore(self, goal):
        self.HScore = int(10 * (abs(goal.xPos - self.xPos) + abs(goal.yPos - self.yPos)))

    def Compare(self, node):
        if self.xPos == node.xPos and self.yPos == node.yPos:
            return True
        else:
            return False