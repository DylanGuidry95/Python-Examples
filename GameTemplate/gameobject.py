'''Base classes and components of a gameobject'''
#pylint: disable=W0403
from vector import Vector2

class Transform(object):
    '''Used to show the position and size of an object in screen space'''
    def __init__(self):
        self.globalposition = Vector2(0, 0)
        self.scale = Vector2(1, 1)

    def scaletransform(self, scale):
        '''Scales the size of the transform'''
        self.scale = Vector2(self.scale.xpos * scale.xpos, self.scale.ypos * scale.ypos)

class Behavior(object):
    '''Base class for all behaviors'''
    def __init__(self, name):
        self.name = name

    def update(self, deltatime):
        '''updats the behavior'''

    def reset(self):
        '''resets the values of the beahvior to default'''

class GameObject(object):
    '''Base class for all gameobjects'''
    def __init__(self, name):
        self.transform = Transform()
        self.name = name
        self.renderer = None
        self.isenabled = True

    def update(self, deltatime):
        '''Updates the objects behaviors'''

    def buttonevent(self, args):
        '''if the gameobject responds to a UIButton click'''

    def draw(self, screen):
        '''Invokes the draw method from the renderer and draws it to the screen'''
        if self.renderer != None:
            self.renderer.draw(screen, self.transform.globalposition)
