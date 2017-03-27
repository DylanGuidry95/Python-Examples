'''gametemplate.py'''
#pylint: disable=E0401
#pylint: disable=E1101
#pylint: disable=W0403
#from gameobject import GameObject
import sys
import pygame

class GameTemplate(object):
    '''pygame object'''
    def __init__(self):
        pygame.init()
        self.deltatime = 0
        self.lasttick = 0

    def _startup(self):
        return True

    def _update(self):
        '''input and time'''
        timer = pygame.time.get_ticks()
        self.deltatime = (timer - self.lasttick)
        self.lasttick = timer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return False
        pygame.display.flip()
        return True

    def _draw(self):
        '''base draw'''

    def _shutdown(self):
        '''shutdown the game properly'''
