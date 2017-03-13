from Utils import *
import sys

size = width, height = 1600, 900
screen = pygame.display.set_mode(size)

rect = Rectangle(screen, [10, 10], WHITE, [30, 30], True)
circle = Circle(screen, [1600, 900], GOLD, 10)
line = Line(screen, [[250, 20], [350, 500]], PURPLE, 10)

rect.draw()
circle.draw()
line.draw()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
    pygame.display.flip()

