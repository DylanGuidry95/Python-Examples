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

class AStar(object):
    def __init__(self, graph):
        self.graph = graph
        self.start = None
        self.goal = None
        self.open = []
        self.close = []
        self.current = None

        self.middleclick = False
        self.rightclick = False
        self.leftclick = False
        self.mtimer = 0.0
        self.rtimer = 0.0
        self.ltimer = 0.0
        self.wasbuttonclicked = [False, False, False]
        self.timers = [0.0, 0.0, 0.0]
        self.deltatime = 0.0
        self.lastTick = 0.0

    def setstartnode(self, node):
        if node in self.graph.nodes:
            self.start = node
            self.start.changestate("start")
            self.current = self.start
            self.open.append(self.start)

    def setgoalnode(self, node):
        if node in self.graph.nodes:
            self.goal = node
            self.goal.changestate("goal")

    def modifywall(self, node):
        if node in self.graph.nodes:
            node.changestate("wall")

    def checknodes(self):
        for graphnode in self.graph.nodes:
            if graphnode.isStart and graphnode != self.start:
                graphnode.changestate("default")
            if graphnode.isGoal and graphnode != self.goal:
                graphnode.changestate("default")

    def enviormentupdate(self):
        timer = pygame.time.get_ticks()
        self.deltatime = (timer - self.lastTick)
        self.lastTick = timer

        for node in self.graph.nodes:
            mxpos, mypos = pygame.mouse.get_pos()
            if node.visual.collisioncheck([mxpos, mypos]):
                if pygame.mouse.get_pressed()[0]:
                    if not self.wasbuttonclicked[0]:
                        self.setstartnode(node)
                        self.wasbuttonclicked[0] = True
                if pygame.mouse.get_pressed()[1]:
                    if not self.wasbuttonclicked[1]:
                        self.modifywall(node)
                        self.wasbuttonclicked[1] = True
                if pygame.mouse.get_pressed()[2]:
                    if not self.wasbuttonclicked[2]:
                        self.setgoalnode(node)
                        self.wasbuttonclicked[2] = True

        for iterator in range(0, 3):
            if self.wasbuttonclicked[iterator]:
                self.timers[iterator] = self.timers[iterator] + self.deltatime
                if self.timers[iterator] > 400:
                    self.timers[iterator] = 0
                    self.wasbuttonclicked[iterator] = False

        self.checknodes()

    def algorithmstep(self):
        if self.current != None:
            for neighbor in self.current.getneighbors(self.graph):
                if neighbor not in self.open:
                    self.open.append(neighbor)
            for opennode in self.open:
                opennode.calcgscore(self.current)
        

class NodeObject(object):
    def __init__(self, position, color):
        self.position = position
        self.visual = Rectangle(screen, [position[0], position[1]], color, [25, 25], 30)

    def drawNode(self):
        self.visual.draw()

    def changecolor(self, color):
        self.visual.changecolor(color)

    def drawtonode(self, node):
        if node != None:
            circle = Circle(screen, [self.drawposition()[0] + (25/2),
                                     self.drawposition()[1] + (25/2)],
                            BLACK, 10)
            line = Line(screen, [[self.drawposition()[0] + (25/2), self.drawposition()[1] + (25/2)],
                                 [node.visual.drawposition()[0] + (25/2),
                                  node.visual.drawposition()[1] + (25/2)]], BLACK, 2)
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
        self.parent = None
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
        if state == "start" and not self.isGoal:
            self.isStart = not self.isStart
            if self.isStart:
                self.visual.changecolor(GREEN)
            else:
                state = "default"
        elif state == "goal"and not self.isStart:
            self.isGoal = not self.isGoal
            if self.isGoal:
                self.visual.changecolor(BLUE)
            else:
                state = "default"
        elif state == "wall"and not self.isGoal and not self.isStart:
            self.isWall = not self.isWall
            if self.isWall:
                self.visual.changecolor(RED)
            else:
                state = "default"
        if state == "default":
            self.isWall = False
            self.isStart = False
            self.isGoal = False
            self.visual.changecolor(WHITE)

    def getneighbors(self, graph):
        neighbors = []

        left = [self.position[0] - 1, self.position[1]]
        topleft = [self.position[0] - 1, self.position[1] + 1]
        top = [self.position[0], self.position[1] + 1]
        topright = [self.position[0] + 1, self.position[1] + 1]
        right = [self.position[0] + 1, self.position[1]]
        bottomright = [self.position[0] + 1, self.position[1] - 1]
        bottom = [self.position[0], self.position[1] - 1]
        bottomleft = [self.position[0] - 1, self.position[1] - 1]
        neighborpositions = [left, topleft, top, topright, right, bottomright, bottom, bottomleft]

        for node in graph.nodes:
            for position in neighborpositions:
                if node.position[0] == position[0] and node.position[1] == position[1]:
                    neighbors.append(node)
                    node.visual.changecolor(YELLOW)
        return neighbors

    def calcgscore(self, node):
        if self.parent is None:
            if node.position[0] == self.position[0] or node.position[1] == self.position[1]:
                node.gscore = 10
            else:
                node.gscore = 14
            self.parent = node
        else:
            tempgscore = self.gscore
            if node.position[0] == self.position[0] or node.position[1] == self.position[1]:
                tempgscore = 10
            else:
                tempgscore = 14
            if tempgscore < self.gscore:
                self.parent = node
        self.visual.drawtonode(self.parent)

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
