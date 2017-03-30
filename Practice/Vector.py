import math

class Vector2(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def __add__(self, rhs):
        return Vector2(self.xpos + rhs.xpos, self.ypos + rhs.ypos)

    def __sub__(self, rhs):
        return Vector2(self.xpos - rhs.xpos, self.ypos - rhs.ypos)

    def __mul__(self, rhs):
        if isinstance(rhs, Vector2):
            return Vector2(self.xpos * rhs.xpos, self.ypos + rhs.ypos)
        else:
            return Vector2(self.xpos * rhs, self.ypos * rhs)

    def __eq__(self, rhs):
        return rhs.xpos == self.xpos and rhs.ypos == self.ypos

    def __ne__(self, rhs):
        return rhs.xpos == self.xpos and rhs.ypos == self.ypos

    def __str__(self):
        return "<" + str(self.xpos) + "," + str(self.ypos) + ">"

    def magnitude(self):
        '''Return the magnitude or lenght of the vector'''
        return math.sqrt((self.xpos * self.xpos) + (self.ypos * self.ypos))

    @staticmethod
    def normalize(vector):
        '''Creates a unit the unit vector of the vector passed in as an argument'''
        return (vector.xpos / vector.magnitude(), vector.ypos / vector.magnitude())

a = Vector2(2,2)
b = Vector2(2,2)
c = a * 4
