from gameobject import *
from shapes import Rectangle
from constants import *

class Agent(GameObject):
    def __init__(self, name):
        GameObject.__init__(self, name)
        self.renderer = Rectangle(WHITE,
                                  Vector2(10, 10))

    def update(self, deltatime):
        self.transform.position = Vector2(10, -10)


    