'''Utils classes for drawing various objects to the screen without having to touch pygame
main use is to be used by students or anyone who is implementing something and doesn't wanna
worry about all of the pygame functions'''
import math
import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
TURQUOISE = (64, 224, 208)
DARKGREEN = (0, 100, 0)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
SALMON = (250, 128, 114)
PINK = (255, 192, 203)
PURPLE = (160, 32, 240)
HOTPINK = (255, 105, 180)
MAROON = (176, 48, 96)
GRAY = (190, 190, 190)
WHITE = (255, 255, 255)
LAVENDER = (230, 230, 250)


class Shape(object):
    '''Base class to be used when drawing shapes'''
    def __init__(self, screen, position, color):
        self.screen = screen
        self.position = position
        self.drawposition = position
        self.color = color

    def changecolor(self, color):
        '''Changes the color that the object will be drawn to the screen'''
        self.color = color

class Rectangle(Shape):
    '''Class used to draw a rectangle object to the screen'''
    def __init__(self, screen, position, color, scale, margin):
        Shape.__init__(self, screen, position, color)
        self.scale = scale
        self.margin = margin

    def draw(self):
        '''Draws a rectangle to the screen based on the value set in the constructor'''
        self.drawposition = [self.position[0] * self.margin, self.position[1] * self.margin]
        pygame.draw.rect(self.screen, self.color,
                         (self.drawposition[0], self.drawposition[1],
                          self.scale[0], self.scale[1]))

class Circle(Shape):
    '''Class used to draw a circle object to the screen'''
    def __init__(self, screen, position, color, radius):
        Shape.__init__(self, screen, position, color)
        self.radius = radius

    def draw(self):
        '''Draws a circle to the screen based on the value set in the constructor'''
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

class Line(Shape):
    '''Class used to draw a line from one point to another'''
    def __init__(self, screen, position, color, width):
        Shape.__init__(self, screen, position, color)
        self.width = width

    def draw(self):
        '''Draws a line to the screen based on the value set in the constructor'''
        pygame.draw.line(self.screen, self.color, self.position[0], self.position[1], self.width)


class Ellipse(Shape):
    '''Class used to draw a ellipse object to the screen'''
    def __init__(self, screen, position, color, scale):
        Shape.__init__(self, screen, position, color)
        self.scale = scale

    def draw(self):
        '''Draws a ellipse to the screen based on the value set in the constructor'''
        pygame.draw.ellipse(self.screen, self.color,
                            (self.position[0], self.position[1], self.scale[0], self.scale[1]))

class Arc(Shape):
    '''Draws an arc to the screen
    angle should be in degrees and is converted to radians later on by the class'''
    def __init__(self, screen, position, color, scale, angles, thickness):
        Shape.__init__(self, screen, position, color)
        self.scale = scale
        self.angles = [angles[0] * math.pi / 180, angles[1] * math.pi / 180]
        self.thickness = thickness

    def draw(self):
        '''Draws an arc to the screen with the initial angle to be index one of the angles list and
        the end angle to be the second index in the angles list'''
        pygame.draw.arc(self.screen, self.color,
                        (self.position[0], self.position[1], self.scale[0], self.scale[1]),
                        self.angles[0], self.angles[1], self.thickness)

class Text(Shape):
    def __init__(self, screen, position, color, text, size):
        Shape.__init__(self, screen, position, color)
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('arial', self.size)

    def draw(self):
        '''Draws text to the screen'''
        render = self.font.render(self.text, 0, self.color[0], self.color[1])
        self.screen.blit(render, (self.position[0], self.position[1]))
