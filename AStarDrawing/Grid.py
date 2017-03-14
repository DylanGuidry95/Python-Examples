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
            
class NodeVisiual(object):
    def __init__(self, position, color):
        self.position = position
        self.visual = Rectangle(screen, [position[0], position[1]], color, [25, 25], 30)

    def drawNode(self):
        self.visual.draw()

    def changecolor(self, color):
        self.visual.changecolor(color)

    def drawtonode(self, node):
        circle = Circle(screen, [self.position[0] + (25/2), self.position[1] + (25/2)],
                             BLACK, 10)
        line = Line(screen, [[self.position[0] + (25/2), self.position[1] + (25/2)],
                             [node.nodevisual.visual.drawposition[0] + (25/2), 
                             node.nodevisual.visual.drawposition[1] + (25/2)]], BLACK, 2)
        circle.draw()
        line.draw()

class Node(object):
    def __init__(self, position):
        self.position = position
        self.nodevisual = NodeVisiual(self.position, WHITE)
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0

    def drawvisual(self):
        self.nodevisual.drawNode()

    def drawconnection(self, node):
        self.nodevisual.drawtonode(node)
    

    def clicked(self):
        self.nodevisual.changecolor(RED)


class NodeInformation(object):
    def __init__(self, position):
        self.position = position

    def drawinformation(self, node):
        gposition = self.position
        hposition = [self.position[0], self.position[1] + 50]
        fposition = [self.position[0], self.position[1] + 100]
        g = Text(screen, gposition, [WHITE, BLACK], "G Score: " + str(node.position[0]), 25)
        h = Text(screen, hposition, [WHITE, BLACK], "H Score:" + str(node.position[1]), 25)
        f = Text(screen, fposition, [WHITE, BLACK], "F Score:" + str(node.fscore), 25)
        g.draw()
        h.draw()
        f.draw()
