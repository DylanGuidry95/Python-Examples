from gameobject import *
from shapes import Rectangle
from constants import *
import random

class Agent(GameObject):
    def __init__(self, name):
        GameObject.__init__(self, name)
        self.renderer = Rectangle(WHITE,
                                  Vector2(10, 10))
        self.target = Vector2(0,0)
        self.velocity = self.transform.globalposition.normalize()

    def boundaries(self):
        ret = Vector2(0,0)
        inbounds = []
        inbounds.append(self.transform.globalposition.xpos > (SCREEN_WIDTH / 2))
        inbounds.append(self.transform.globalposition.xpos < -(SCREEN_WIDTH / 2))
        inbounds.append(self.transform.globalposition.xpos > (SCREEN_HEIGHT / 2))
        inbounds.append(self.transform.globalposition.xpos < -(SCREEN_HEIGHT / 2))
        for condition in inbounds:
            if condition:
                ret = Vector2(random.randint(-10, 10), random.randint(-10, 10))
        return ret


    def update(self, deltatime):
        self.velocity = Vector2.add(self.velocity, self.boundaries().normalize())
        if self.velocity > 10:
            self.velocity = self.velocity.normalize()
        self.transform.globalposition = Vector2.add(self.transform.globalposition,
                                                    self.velocity)


        