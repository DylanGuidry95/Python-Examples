'''Vector Math Utils classes'''
import math
from Utils import *

SIZE = WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode(SIZE)

class Vector2(object):
    '''Vector2 Math class'''
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def maginitude(self):
        '''Returns the magnitude of the vector'''
        return math.sqrt((self.xpos * self.xpos) + (self.ypos * self.ypos))

    def normalize(self):
        '''Returns a unit vector'''
        return Vector2(self.xpos / self.maginitude(), self.ypos / self.maginitude())

    def scale(self, scalar):
        '''Scales the value of the vector'''
        return Vector2(self.xpos * scalar, self.ypos * scalar)

    @staticmethod
    def add(rhs, lhs):
        '''Return a new vecotr with the sum of the two vectors passed'''
        return Vector2(rhs.xpos + lhs.xpos, rhs.ypos + lhs.ypos)

    @staticmethod
    def subtract(rhs, lhs):
        '''Return a new vector with the difference between two vectors'''
        return Vector2(rhs.xpos - lhs.xpos, rhs.ypos - lhs.ypos)


class Agent(object):
    '''Moveable object'''
    def __init__(self, position):
        self.position = position
        self.maxvelocity = 2.0
        self.velocity = position.normalize()
        self.targetposition = Vector2(WIDTH / 2, HEIGHT / 2)

    def update(self, deltatime):
        '''Updates the position of the agent'''
        self.velocity = self.velocity.scale(deltatime)
        if self.velocity.maginitude() > self.maxvelocity:
            self.velocity = self.velocity.normalize()
        self.position = Vector2.add(self.position, self.velocity)
        self.drawagent()

    def drawagent(self):
        '''Draws a visual to the screen at the objects position'''
        display = Rectangle(SCREEN, [self.position.xpos, self.position.ypos],
                            WHITE, [10, 10], 10)
        display.draw()

    def settarget(self, position):
        '''Sets the value of the target position'''
        self.targetposition = position

deltatime = 0.0
lasttick = 0.0

newAgent = Agent(Vector2(450,100))

while not pygame.key.get_pressed()[pygame.K_i]:
    timer = pygame.time.get_ticks()
    deltatime = (timer - lasttick)
    lasttick = timer

    newAgent.update(deltatime)


