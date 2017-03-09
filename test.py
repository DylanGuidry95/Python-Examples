class Node(object):
    def __init__(self, xPos, yPos, value):
        self.xPos = xPos
        self.yPos = yPos
        self.value = value
        self.neighbors = []

    def Compare(self,node):
        if self.xPos == node.xPos and self.yPos == node.yPos:
            return True
        else:
            return False

class Grid(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []
        self.GenGrid()

    def GenGrid(self):        
        for i in range(0,self.width + 1):
            for j in range(0,self.height):
                node = Node(i,j, " ")        
                self.nodes.append(node)

    def PrintGrid(self):
        row = ""
        x = ""
        y = ""
        i = 0
        for node in self.nodes:
            if i % self.width == 0:
                print row, "\n"
                row = ""
            x = str(node.xPos)
            y = str(node.yPos)
            row += "["+ node.value +"]"
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

         adj = [left,top,right,bottom, topLeft, topRight, bottomRight, bottomLeft]

         if node in self.nodes:
             for n in self.nodes:
                 for a in adj:
                     if n.Compare(a):
                        node.neighbors.append(n)

         print  "Current: [", node.xPos, "," , node.yPos, "]" 
         for n in node.neighbors:
            print "[", n.xPos, "," , n.yPos, "]"                     
                 
             

class Algorithm(object):
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.open = []
        self.close = []
        self.start = start
        self.goal = goal
        self.current = start
        
    
        

def main():
    grid = Grid(10,10)
    
    grid.GetNeighbor(grid.nodes[3])


    
main()