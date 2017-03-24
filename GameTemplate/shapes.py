'''Various shapes to make drawing easier'''
import pygame
from vector import Vector2
from constants import *

def screentoworld(position):
    '''Converts the vecotr passed in to a vector in screen space'''
    screenx = position.xpos + (SCREEN_WIDTH / 2)
    screeny = position.ypos + (SCREEN_HEIGHT / 2)
    return Vector2(screenx, screeny)

class Shape(object):
    '''Base class to be used when drawing shapes'''
    def __init__(self, color):
        self.color = color

    def changecolor(self, color):
        '''Changes the color that the object will be drawn to the screen'''
        self.color = color

class Rectangle(Shape):
    '''Class used to draw a rectangle object to the screen'''
    def __init__(self, color, scale):
        Shape.__init__(self, color)
        self.scale = scale

    def draw(self, screen, position):
        '''Draws a rectangle to the screen based on the value set in the constructor'''
        pos = screentoworld(position)
        pygame.draw.rect(screen, self.color,
                         (pos.xpos, pos.ypos,
                          self.scale.xpos, self.scale.ypos))

    def checkposition(self, position):
        '''Checks to ensure the object is being drawn in screen space'''
        pos = screentoworld(position)
        if pos.xpos > SCREEN_WIDTH:
            pos.xpos = SCREEN_WIDTH
        if pos.ypos > SCREEN_HEIGHT:
            pos.ypos = SCREEN_HEIGHT
        if pos.xpos < 0:
            pos.ypos = 0
        if pos.ypos < 0:
            pos.ypos = 0


class Line(Shape):
    '''Class used to draw a line from one point to another'''
    def __init__(self, color, width):
        Shape.__init__(self, color)
        self.width = width

    def draw(self, screen, position):
        '''Draws a line to the screen based on the value set in the constructor'''
        startpos = screentoworld(position[0])
        endpos = screentoworld(position[1])
        pygame.draw.line(screen, self.color, (startpos.xpos, startpos.ypos),
                         (endpos.xpos, startpos.ypos), self.width)
