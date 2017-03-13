from Grid import Grid

class AStar(object):
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.current = start
        self.current.SetHScore(self.goal)
        self.open = [self.start]
        self.close = []

    def Step(self):
        if self.goal in self.close:
            return
        if self.open.count == 0:
            return

        self.current = self.open[0]

        for node in self.grid.GetNeighbor(self.current):
            node.SetGScore(self.current)

        for child in self.current.children:
            if child in self.close:
                continue
            else:
                self.open.append(child)

        if self.current in self.open:
            self.open.remove(self.current)
            self.close.append(self.current)

        self.SortOpenList()

        for node in self.open:
            self.grid.nodes[self.current].DrawNode((255, 255, 0))
            node.SetGScore(self.current)
            node.SetHScore(self.goal)
            node.SetFScore()

        self.grid.nodes[self.current].DrawNode((255, 0, 0))
        self.grid.nodes[self.start].DrawNode((0, 255, 0))
        self.grid.nodes[self.goal].DrawNode((0, 0, 255))

    def SortOpenList(self):
        for node in self.grid.nodes:
            for nodeCheck in self.grid.nodes:
                if node.FScore < nodeCheck.FScore:
                    tempNode = node
                    node = nodeCheck
                    nodeCheck = tempNode
