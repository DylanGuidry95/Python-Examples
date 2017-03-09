from Grid import Grid

class AStar(object):
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.open = []
        self.close = []
        self.start = start
        self.goal = goal
        self.current = start
        self.current.SetHScore(self.goal)

    def Step(self):
        self.open = self.grid.GetNeighbor(self.current)
        if self.current in self.open:
            self.open.remove(self.current)
            self.close.append(self.current)
        for node in self.grid.nodes:
            node.parent = self.current
            node.SetGScore()
            node.SetHScore(self.goal)
            node.SetFScore()            

    def SortOpenList(self):
        for node in self.grid.nodes:
            for nodeCheck in self.grid.nodes:
                if node.FScore < nodeCheck.FScore:
                    tempNode = node
                    node = nodeCheck
                    nodeCheck = tempNode
        