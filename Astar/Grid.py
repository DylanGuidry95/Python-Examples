from Node import Node
from Node import NodeVisual

class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = {}
        self.GenGrid()

    def GenGrid(self):
        for i in range(0, self.width + 1):
            for j in range(0, self.height):
                node = Node(i, j, " ")
                self.nodes[node] = NodeVisual(i, j)

    def PrintGrid(self):
        row = ""
        i = 0
        for node in self.nodes:
            if i % self.width == 0:
                print row, "\n"
                row = ""
            row += "[" + node.value + "]"
            i += 1

    def GetNeighbor(self, node):
        left = Node(node.xPos + 1, node.yPos, 0)
        top = Node(node.xPos, node.yPos + 1, 0)
        right = Node(node.xPos - 1, node.yPos, 0)
        bottom = Node(node.xPos, node.yPos - 1, 0)
        topLeft = Node(node.xPos + 1, node.yPos + 1, 0)
        topRight = Node(node.xPos - 1, node.yPos + 1, 0)
        bottomRight = Node(node.xPos - 1, node.yPos - 1, 0)
        bottomLeft = Node(node.xPos + 1, node.yPos - 1, 0)

        adj = [left, top, right, bottom, topLeft,
               topRight, bottomRight, bottomLeft]

        neighbors = []       

        if node in self.nodes:
            for n in self.nodes:
                for a in adj:
                    if n.Compare(a):
                        neighbors.append(n)

        return neighbors
    