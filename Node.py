class Node(object):
    def __init__(self, xPos, yPos, value):
        self.xPos = xPos
        self.yPos = yPos
        self.value = value
        self.neighbors = []

    def Compare(self, node):
        if self.xPos == node.xPos and self.yPos == node.yPos:
            return True
        else:
            return False