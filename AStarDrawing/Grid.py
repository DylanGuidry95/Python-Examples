'''All modules that modify the graph visualy and the information in it'''
from Node import Node
from Node import NodeInformation

class Graph(object):
    '''Object that stores nodes and assigns them position values'''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []

    def setupgraph(self):
        '''Craetes the nodes in the graph'''
        for xpos in range(0, self.width):
            for ypos in range(0, self.height):
                self.nodes.append(Node([xpos, ypos]))

    def drawgraph(self):
        '''Draws the nodes in the graph to the screen'''
        for node in self.nodes:
            node.drawvisual()

class AStar(object):
    '''Astar algorithm implementation'''
    def __init__(self, graph):
        self.graph = graph
        self.start = None
        self.goal = None
        self.open = []
        self.close = []
        self.current = None
        self.nodeinfo = NodeInformation([0, 750])

    def setstartnode(self, node):
        '''Trys to set the node passed in as the starting node'''
        if node in self.graph.nodes:
            self.start = node
            self.start.changestate("start")
            self.current = self.start
            self.open.append(self.start)

    def setgoalnode(self, node):
        '''Trys to set the node passed in as the goal node'''
        if node in self.graph.nodes:
            self.goal = node
            self.goal.changestate("goal")

    def modifywall(self, node):
        '''Trys to add or remove walls on the graph'''
        if node in self.graph.nodes:
            node.changestate("wall")

    def checknodes(self):
        '''Checks the states of the nodes to ensure they are set properly'''
        for graphnode in self.graph.nodes:
            if graphnode.isstart and graphnode != self.start:
                graphnode.changestate("default")
            if graphnode.isgoal and graphnode != self.goal:
                graphnode.changestate("default")

    def enviormentupdate(self):
        '''Updates the visuals on screen'''
        self.checknodes()

    def algorithmstep(self):
        '''Iterates through the algorithm until win condition'''
        if self.current != None:
            for neighbor in self.current.getneighbors(self.graph):
                if neighbor not in self.open:
                    self.open.append(neighbor)
            for opennode in self.open:
                if opennode != self.current:
                    opennode.calcgscore(self.current)
