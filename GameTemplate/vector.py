'''Simple vector classes'''
import math

class Vector2(object):
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def magnitude(self):
        '''Returns the magnitude of the vector'''
        return math.sqrt((self.xpos * self.xpos) + (self.ypos * self.ypos))

    def normalize(self):
        '''Returns a unit vector'''
        if self.magnitude() == 0:
            return Vector2(self.xpos / 1, self.ypos / 1)
        else:
            return Vector2(self.xpos / self.magnitude(), self.ypos / self.magnitude())

    def multiplication(self, scalar):
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

    @staticmethod
    def equalto(rhs, lhs):
        '''Compares two vectors to see if they are the same'''
        return rhs.xpos == lhs.xpos and rhs.ypos == lhs.ypos

    @staticmethod
    def distance(rhs, lhs):
        '''Gets the distance from one vector to another'''
        return Vector2.subtract(rhs, lhs).magnitude()
