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
        vecotor = (self.transform.globalposition - self.target).normalize().scale(5)
        force = vecotor - self.velocity
        return force

    def update(self, deltatime):
        self.velocity = self.velocity + self.seek().scale(deltatime)
        if self.velocity.magnitude() > 10:
            self.velocity = self.velocity.normalize()
        self.transform.globalposition = (self.transform.globalposition
                                         + self.velocity).scale(deltatime)
