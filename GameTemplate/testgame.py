'''Test game loop'''
#pylint: disable=W0403
import pygame
from gametemplate import GameTemplate
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from constants import WHITE
from shapes import Line
from shapes import Rectangle
from vector import Vector2
from shapes import worldtoscreen

class TestGame(GameTemplate):
    '''Test game loop'''
    def __init__(self, name):
        self.name = name
        self.gameobjects = []
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        super(TestGame, self).__init__()

    def addnewobject(self, gameobject):
        '''Adds a new object to the game'''
        if gameobject not in self.gameobjects:
            self.gameobjects.append(gameobject)

    def update(self):
        '''invokes the update loop on all objects'''
        for gameobject in self.gameobjects:
            gameobject.update(self.deltatime)
        return super(TestGame, self)._update()

    def draw(self):
        '''Draws all objects that are in the gameobjects list to the screen'''
        self.screen.fill((0, 0, 0))
        yaxis = Line(WHITE, 5)
        yaxis.draw(self.screen, [Vector2(0, -(SCREEN_HEIGHT / 2)),
                                 Vector2(0, (SCREEN_HEIGHT / 2))])
        xaxis = Line(WHITE, 5)
        xaxis.draw(self.screen, [Vector2(-(SCREEN_WIDTH / 2), 0),
                                 Vector2(SCREEN_WIDTH / 2, 0)])
        mxpos, mypos = pygame.mouse.get_pos()
        mouse = Rectangle(WHITE, Vector2(25, 25))
        mpos = worldtoscreen(Vector2(mxpos, mypos))
        mpos = mpos.multiplication(-1)
        mouse.draw(self.screen, mpos)


        for gameobject in self.gameobjects:
            gameobject.draw(self.screen)

    def run(self):
        '''Updates and draw objects to the screen each loop'''
        if super(TestGame, self)._startup():
            while self.update():
                self.draw()
        super(TestGame, self)._shutdown()
