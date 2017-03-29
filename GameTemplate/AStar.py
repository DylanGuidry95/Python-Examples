'''Astar.py'''
from vector import Vector2

class Graph(object):
    '''Graph'''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []
        self.gengraph()

    def gengraph(self):
        '''generates the graph'''
        nodecount = 0
        for row in range(0, self.width):
            for col in range(0, self.height):
                self.nodes.append(Node(Vector2(col, row), str(nodecount)))
                nodecount = nodecount + 1

    def getnode(self, nodeval):
        '''Checks to see if a node with the nodevalue passed in is in the graph'''
        for node in self.nodes:
            if node.value == nodeval:
                return node
        return None

class Node(object):
    '''Node'''
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

    def calcgscore(self, node, inlist):
        '''Calculates the gscore for the node based on the position of the node passed in'''
        tentativeg = 0
        if self.position.xpos == node.position.xpos or self.position.ypos == node.position.ypos:
            tentativeg = 10
        else:
            tentativeg = 14
        if not inlist:
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
    '''Astar'''
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

    def retrace(self):
        '''Retraces the path from the goal node to the start node
        by following the node parents and returns a list of all nodes
        travered'''
        current = self.endnode
        path = []
        while current is not None:
            path.append(current)
            current = current.parent
        return path

    def algorithm(self):
        '''AStar algorithm implementation'''
        if self.begnode is None or self.endnode is None:
            return None
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


def getcorrectpath(testcase):
    '''Gets path from a text file'''
    path = open("test.txt", "r")
    vectors = []
    for line in path:
        if "#" in line:
            continue
        if testcase + "=answer=" in line:
            for i in range(0, len(line)):
                value = ""
                if line[i] == '<':
                    while line[i] != '>':
                        value = value + line[i]
                        i = i + 1
                    value = value + line[i]
                    vectors.append(value)
    return vectors

def enviormentsetup(line, graph, algorithm):
    '''Modifies the testing enviorment'''
    for iterator in range(0, len(line)):
        if line[iterator] == 'G':
            iterator = iterator + 2
            nodevalue = ""
            while line[iterator] != ';':
                nodevalue = nodevalue + line[iterator]
                iterator = iterator + 1
            algorithm.setgoal(graph.getnode(nodevalue))
        if line[iterator] == 'S':
            iterator = iterator + 2
            nodevalue = ""
            while line[iterator] != ';':
                nodevalue = nodevalue + line[iterator]
                iterator = iterator + 1
            algorithm.setstart(graph.getnode(nodevalue))
        if line[iterator] == 'W':
            iterator = iterator + 2
            nodevalue = ""
            while line[iterator] != ';':
                nodevalue = nodevalue + line[iterator]
                iterator = iterator + 1
            graph.getnode(nodevalue).iswalkable = False

def checkalgorithm():
    '''Sets up graphs and tests them based on value found in a text file'''
    enviorment = open("test.txt")
    lines = enviorment.readlines()
    answer = open("answer.txt", "w").close()
    testnum = 0
    answer = open("answer.txt", "a")
    for line in lines:
        if "#" in line:
            continue
        if "==>" in line:
            testnum = testnum + 1
            graph = Graph(10, 10)
            algo = AStarAlgorithm(graph)
            enviormentsetup(line, graph, algo)
            answer.write(line)
            answer.write("Test" + str(testnum) + "=path=")
            path = algo.algorithm()
            correct = getcorrectpath("Test" + str(testnum))
            numcorrect = 0
            if path is not None:
                for node in range(0, len(path)):
                    if str(path[node].position) == correct[node]:
                        numcorrect = numcorrect + 1
                    answer.write(str(path[node].position))
            answer.write('\n')
            correctpercent = (float(numcorrect) / float(len(correct))) * 100
            answer.write("Correct:" + str(correctpercent))
            answer.write('\n')
    answer.close()

checkalgorithm()
