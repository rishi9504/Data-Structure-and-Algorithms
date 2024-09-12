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
    
    def insertLeft(self, data):
        self.left = BinaryTreeNode(data)
        return self.left

    def insertRight(self, data):
        self.right = BinaryTreeNode(data)
        return self.right
    
    def insertUsingLevelOrder(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insertUsingLevelOrder(data)
            else:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insertUsingLevelOrder(data)

    def deleteTree(self,root):
        if root is None:
            return
        self.deleteTree(root.left)
        self.deleteTree(root.right)
        del root
        root.data = None


    

import unittest


class TestBinaryTreeNode(unittest.TestCase):
    def test_init(self):
        n = BinaryTreeNode(1)
        self.assertEqual(n.data, 1)
        self.assertIsNone(n.left)
        self.assertIsNone(n.right)

    def test_str(self):
        n = BinaryTreeNode(1)
        self.assertEqual(str(n), '1')

    def test_getData(self):
        n = BinaryTreeNode(1)
        self.assertEqual(n.getData(), 1)

    def test_setData(self):
        n = BinaryTreeNode(1)
        n.setData(2)
        self.assertEqual(n.getData(), 2)

    def test_getLeft(self):
        n = BinaryTreeNode(1)
        self.assertIsNone(n.getLeft())

    def test_getRight(self):
        n = BinaryTreeNode(1)
        self.assertIsNone(n.getRight())


    def test_getLeft(self):
        n = BinaryTreeNode(1)
        self.assertIsNone(n.getLeft())

    def test_getRight(self):
        n = BinaryTreeNode(1)
        self.assertIsNone(n.getRight())

    def test_insertLeft(self):
        n = BinaryTreeNode(1)
        left = n.insertLeft(2)
        self.assertEqual(left.data, 2)
        self.assertEqual(n.getLeft().data, 2)

    def test_insertRight(self):
        n = BinaryTreeNode(1)
        right = n.insertRight(2)
        self.assertEqual(right.data, 2)
        self.assertEqual(n.getRight().data, 2)
    


if __name__ == '__main__':
    unittest.main()
