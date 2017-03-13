'''Module used to draw objects to the screen'''
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
        self.color = color

    def changecolor(self, color):
        '''Changes the color that the object will be drawn to the screen'''
        self.color = color

class Rectangle(Shape):
    '''Class used to draw a rectangle object to the screen'''
    def __init__(self, screen, position, color, scale, isoutline):
        Shape.__init__(self, screen, position, color)
        self.scale = scale
        self.isoutline = isoutline

    def draw(self):
        '''Draws a rectangle to the screen based on the value set in the constructor'''
        if self.isoutline:
            pygame.draw.rect(self.screen, self.color,
                             (self.position[0], self.position[1], self.scale[0], self.scale[1]), 2)
        else:
            pygame.draw.rect(self.screen, self.color,
                             (self.position[0], self.position[1], self.scale[0], self.scale[1]))

class Circle(Shape):
    '''Class used to draw a circle object to the screen'''
    def __init__(self, screen, position, color, radius):
        Shape.__init__(self, screen, position, color)
        self.radius = radius

    def draw(self):
        '''Draws a circle to the screen based on the value set in the constructor'''
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

class Line(Shape):
    def __init__(self, screen, position, color, width):
        Shape.__init__(self, screen, position, color)
        self.width = width

    def draw(self):
        pygame.draw.line(self.screen, self.color, self.position[0], self.position[1], self.width)

