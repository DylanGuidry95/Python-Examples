'''Modules that control the main game loop'''
import sys
import pygame

class GameLoop(object):
    '''Controls the game loop and calcualtes delta time for the application'''
    def __init__(self):
        self.deltatime = 0.0
        self.lasttick = 0.0
        pygame.init()

    def update(self):
        '''Handles the execution of the application'''
        self.deltatime()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                return False

        pygame.display.flip()
        pygame.display.flip()
        return True

    def calcdeltatime(self):
        '''Calculates the delta time for the application'''
        timer = pygame.time.get_ticks()
        self.deltatime = (timer - self.lasttick)
        self.lasttick = timer
    
class AStarInteraction(object):
    def __init__(self, algorithm):
        self.algorithm = algorithm
