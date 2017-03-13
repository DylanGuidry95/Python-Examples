from Utils import*

size = width, height = 1600, 900
screen = pygame.display.set_mode(size)

class Graph(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []

    def setupgraph(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.nodes.append(Node([x, y]))

    def drawgraph(self):
        for node in self.nodes:
            node.drawvisual()
            

class Node(object):
    def __init__(self, position):
        self.position = position
        self.nodevisual = Rectangle(screen, [position[0], position[1]], WHITE, [25, 25], 30)
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0    

    def drawvisual(self):
        self.nodevisual.draw()

    def clicked(self):
        self.nodevisual.changecolor(RED)


class NodeInformation(object):
    def __init__(self, position):
        self.position = position

    def drawinformation(self, node):
        gposition = self.position
        hposition = [self.position[0], self.position[1] + 50]
        fposition = [self.position[0], self.position[1] + 100]
        g = Text(screen, gposition, [WHITE, BLACK], "G Score: " + str(node.gscore), 25)
        h = Text(screen, hposition, [WHITE, BLACK], "H Score:" + str(node.hscore), 25)
        f = Text(screen, fposition, [WHITE, BLACK], "F Score:" + str(node.fscore), 25)
        g.draw()
        h.draw()
        f.draw()
