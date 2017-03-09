from Grid import Grid

class Astar(object):
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.open = []
        self.close = []
        self.start = start
        self.goal = goal
        self.current = start