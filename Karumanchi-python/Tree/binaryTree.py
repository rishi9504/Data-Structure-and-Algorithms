# Binary Tree class and its methods

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)
    
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right    
