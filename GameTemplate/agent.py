'''Agent'''
import random
import pygame
from GameTemplate.gameobject import GameObject
from GameTemplate.vector import Vector2
from GameTemplate.shapes import Rectangle
from GameTemplate.constants import *


class Agent(GameObject):
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
        return Vector2.subtract(self.transform.globalposition, self.target).normalize()

    def update(self, deltatime):
        self.velocity = Vector2.add(self.velocity, self.boundaries())
        self.velocity = Vector2.add(self.velocity, self.seek())
        if self.velocity > 10:
            self.velocity = self.velocity.normalize()
        self.transform.globalposition = Vector2.add(self.transform.globalposition,
                                                    self.velocity)
