'''Various shapes to make drawing easier'''
import pygame
from vector import Vector2
from constants import *

def screentoworld(position):
    '''Converts the vecotr passed in to a vector in screen space'''
    screenx = (position.xpos) + (SCREEN_WIDTH / 2)
    screeny = ((position.ypos * -1)) + (SCREEN_HEIGHT / 2)
    return Vector2(screenx, screeny)

def worldtoscreen(position):
    '''Convertes the passed in to world space'''
    worldx = (position.xpos * -1) + (SCREEN_WIDTH / 2)
    worldy = ((position.ypos)) - (SCREEN_HEIGHT / 2)
    return Vector2(worldx, worldy)

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
                         (pos.xpos - (self.scale.xpos / 2), pos.ypos - (self.scale.ypos / 2),
                          self.scale.xpos, self.scale.ypos))


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
                         (endpos.xpos, endpos.ypos), self.width)
