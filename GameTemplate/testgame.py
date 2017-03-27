from gametemplate import GameTemplate
from constants import *
import pygame
from shapes import Line
from vector import Vector2

class TestGame(GameTemplate):
    def __init__(self, name):
        self.name = name
        self.gameobjects = []
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        super(TestGame, self).__init__()

    def addnewobject(self, gameobject):
        if gameobject not in self.gameobjects:
            self.gameobjects.append(gameobject)

    def update(self):
        for gameobject in self.gameobjects:
            gameobject.update(self.deltatime)
        return super(TestGame, self)._update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        yaxis = Line(WHITE, 5)
        yaxis.draw(self.screen, [Vector2(0, -(SCREEN_HEIGHT / 2)),
                                 Vector2(0, (SCREEN_HEIGHT / 2))])
        xaxis = Line(WHITE, 5)
        xaxis.draw(self.screen, [Vector2(-(SCREEN_WIDTH / 2), 0),
                                 Vector2(SCREEN_WIDTH / 2, 0)])
        for gameobject in self.gameobjects:
            gameobject.draw(self.screen)
    
    def run(self):
        if super(TestGame, self)._startup():
            while self.update():
                self.draw()
        super(TestGame, self)._shutdown()