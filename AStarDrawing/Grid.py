from Utils import*

size = width, height = 1600, 900
screen = pygame.display.set_mode(size)

middleclick = False
rightclick = False
leftclick = False

mtimer = 0
rtimer = 0
ltimer = 0

deltatime = 0.0
lastTick = 0.0

class Graph(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []
        lastTick = 0.0

    def setupgraph(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.nodes.append(Node([x, y]))

    def drawgraph(self):
        for node in self.nodes:
            node.drawvisual()

class AStar(object):
    def __init__(self, graph):
        self.graph = graph
        self.start = None
        self.goal = None

    def setstartnode(self, node):
        if node in self.graph.nodes:
            if self.start == None:
                self.start = node
            else:
                self.start.changestate("start")
                self.start = node
                self.start.changestate("start")

    def setgoalnode(self, node):
        if node in self.graph.nodes:
            if self.start == None:
                self.start = node
            else:
                self.start.changestate("goal")
                self.start = node
                self.start.changestate("goal")

    def modifywall(self, node):
        if node in self.graph.nodes:
            node.changestate("wall")

    def update(self):               
        timer = pygame.time.get_ticks()
        deltatime = (timer - lastTick)
        lastTick = timer 

        for node in self.graph.nodes:
            mxpos, mypos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[1] and not middleclick:
                middleclick = True
                if node.visual.collisioncheck([mxpos, mypos]):
                    self.modifywall(node)        
        if middleclick == True:
            mtimer = mtimer + (deltatime)
        if mtimer > 400:
            mtimer = 0
            middleclick = False


class NodeObject(object):
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

    def drawposition(self):
        return self.visual.drawposition

    def collisioncheck(self, colpos):
        if colpos[0] > self.drawposition()[0] and colpos[0] < self.drawposition()[0] + 25:
            if colpos[1] > self.drawposition()[1] and colpos[1] < self.drawposition()[1] + 25:
                return True
        else:
            return False

class Node(object):
    def __init__(self, position):
        self.position = position
        self.visual = NodeObject(self.position, WHITE)
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.isWall = False
        self.isGoal = False
        self.isStart = False

    def drawvisual(self):
        self.visual.drawNode()

    def drawconnection(self, node):
        self.visual.drawtonode(node)

    def changestate(self, state):
        if state == "start":
            self.isStart = not self.isStart
            if self.isStart:
                self.visual.changecolor(GREEN)
            else:
                self.visual.changecolor(WHITE)
        elif state == "goal":
            self.isGoal = not self.isGoal
            if self.isGoal:
                self.visual.changecolor(BLUE)
            else:
                self.visual.changecolor(WHITE)
        elif state == "wall":
            self.isWall = not self.isWall
            if self.isWall:
                self.visual.changecolor(RED)
            else:
                self.visual.changecolor(WHITE)

class NodeInformation(object):
    def __init__(self, position):
        self.position = position

    def drawinformation(self, node):
        gposition = self.position
        hposition = [self.position[0], self.position[1] + 50]
        fposition = [self.position[0], self.position[1] + 100]
        gtext = Text(screen, gposition, [WHITE, BLACK], "G Score: " + str(node.position[0]), 25)
        htext = Text(screen, hposition, [WHITE, BLACK], "H Score:" + str(node.position[1]), 25)
        ftext = Text(screen, fposition, [WHITE, BLACK], "F Score:" + str(node.fscore), 25)
        gtext.draw()
        htext.draw()
        ftext.draw()
