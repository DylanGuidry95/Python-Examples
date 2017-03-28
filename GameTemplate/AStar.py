from gameobject import GameObject
from vector import Vector2

class Graph(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []

    def gengraph(self):
        '''generates the graph'''
        nodecount = 0
        for row in range(0, self.width):
            for col in range(0, self.height):
                self.nodes.append(Node(Vector2(col, row), nodecount))
                nodecount = nodecount + 1

    def getnode(self, nodeval):
        for node in self.nodes:
            if node.value == nodeval:
                return node
        return None

class Node(object):
    def __init__(self, position, value):
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.position = position
        self.parent = None
        self.value = value
        self.iswalkable = True

    def getneighbors(self, graph):
        '''Gets all the neighbors of this node in the graph passed in'''
        neighbors = []
        validpositions = []
        validpositions.append(self.position + Vector2(1, 0)) #Right
        validpositions.append(self.position + Vector2(1, 1)) #TopRight
        validpositions.append(self.position + Vector2(0, 1)) #Top
        validpositions.append(self.position + Vector2(-1, 1)) #TopLeft
        validpositions.append(self.position + Vector2(-1, 0)) #Left
        validpositions.append(self.position + Vector2(-1, -1)) #BotLeft
        validpositions.append(self.position + Vector2(0, -1)) #Bot
        validpositions.append(self.position + Vector2(1, -1)) #BotRight
        for node in graph.nodes:
            for position in validpositions:
                if node.position == position:
                    neighbors.append(node)
        return neighbors

    def calcgscore(self, node, isinlist):
        '''Calculates the gscore for the node based on the position of the node passed in'''
        tentativeg = 0
        if self.position.xpos == node.position.xpos or self.position.ypos == node.position.ypos:
            tentativeg = 10
        else:
            tentativeg = 14
        if not isinlist:
            self.gscore = node.gscore + tentativeg
            self.parent = node
        else:
            if self.gscore > tentativeg:
                self.gscore = node.gscore + tentativeg
                self.parent = node

    def calchscore(self, node):
        '''Calculates the manhatan distance from this node to the node passed in'''
        self.hscore = 10 * (abs(self.position.xpos - node.position.xpos) +
                            abs(self.position.ypos - node.position.ypos))

    def calcfscore(self):
        '''Calculates the fscore for the current node'''
        self.fscore = self.gscore + self.hscore


class AStarAlgorithm(object):
    def __init__(self, graph):
        self.graph = graph
        self.begnode = None
        self.endnode = None
        self.openlist = []
        self.closelist = []

    def setstart(self, node):
        '''Tries to set the starting node'''
        if self.graph.getnode(node.value):
            self.begnode = node

    def setgoal(self, node):
        '''Tries to set the starting node'''
        if self.graph.getnode(node.value):
            self.endnode = node

    def sortopenlist(self):
        for node in self.openlist:
            for compare in self.openlist:
                if node.fscore < compare.fscore:
                    temp = node
                    node = compare
                    compare = temp

    def retrace(self):
        current = self.endnode
        path = []
        while current is not None:
            path.append(current)
            current = current.parent
        return path

    def algorithm(self):
        if self.begnode is None or self.endnode is None:
            return "No Start or Goal set"
        current = self.begnode
        self.openlist.append(current)
        while len(self.openlist) > 0:
            self.openlist.remove(current)
            self.closelist.append(current)
            neighbors = current.getneighbors(self.graph)
            for node in neighbors:
                if node not in self.openlist:
                    if node not in self.closelist:
                        if node.iswalkable:
                            self.openlist.append(node)
                            node.calcgscore(current, False)
                else:
                    if node not in self.closelist:
                        node.calcgscore(current, True)
                node.calchscore(self.endnode)
                node.calcfscore()
            self.openlist.sort(key=lambda node: node.fscore)
            current = self.openlist[0]
            if self.endnode in self.closelist:
                return self.retrace()
        return None


graph = Graph(10, 10)
graph.gengraph()
algo = AStarAlgorithm(graph)
algo.setgoal(graph.getnode(47))
algo.setstart(graph.getnode(43))
graph.getnode(35).iswalkable = False
graph.getnode(45).iswalkable = False
graph.getnode(55).iswalkable = False

bad = []
for node in graph.nodes:
    if not node.iswalkable:
        bad.append(node)


test = algo.algorithm()
for node in test:
    print node.position