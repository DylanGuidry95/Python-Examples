'''Agent'''
#pylint: disable=W0403
import random
import pygame
from gameobject import GameObject
from vector import Vector2
from shapes import Rectangle
from shapes import worldtoscreen
from constants import WHITE
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH

class Agent(GameObject):
    '''agent object'''
    def __init__(self, name):
        GameObject.__init__(self, name)
        self.renderer = Rectangle(WHITE,
                                  Vector2(10, 10))
        self.target = Vector2(0, 0)
        self.velocity = self.transform.globalposition.normalize()

    def boundaries(self):
        '''Force that keeps the agent in screen view'''
        ret = Vector2(0, 0)
        inbounds = []
        inbounds.append(self.transform.globalposition.xpos > (SCREEN_WIDTH / 2))
        inbounds.append(self.transform.globalposition.xpos < -(SCREEN_WIDTH / 2))
        inbounds.append(self.transform.globalposition.ypos > (SCREEN_HEIGHT / 2))
        inbounds.append(self.transform.globalposition.ypos < -(SCREEN_HEIGHT / 2))
        for condition in inbounds:
            if condition:
                ret = Vector2(random.randint(-10, 10), random.randint(-10, 10))
        return ret

    def seek(self):
        '''Seeking force to drive the agent toward a location'''
        mxpos, mypos = pygame.mouse.get_pos()
        self.target = Vector2(mxpos, mypos)
        self.target = worldtoscreen(self.target)
        displacement = Vector2.subtract(self.transform.globalposition, self.target)
        steer = displacement.multiplication(10).normalize()
        return Vector2(steer.xpos - self.velocity.xpos, steer.ypos - self.velocity.ypos)

    def update(self, deltatime):
        self.velocity = Vector2.add(self.velocity, self.seek())
        if self.velocity.magnitude() > 5:
            self.velocity = self.velocity.normalize()
        print str(self.velocity.xpos) + "," + str(self.velocity.ypos)
        self.transform.globalposition = Vector2.add(self.transform.globalposition,
                                                    self.velocity)
