import queue
from binaryTree import BinaryTreeNode
# give an algorithm for finding the sum of all the nodes in the binary tree
# time complexity O(n)

def sumOfBinaryTree(root):
    if root is None:
        return 0
    return root.data + sumOfBinaryTree(root.left) + sumOfBinaryTree(root.right)

# give an algorithm for finding the sum of all the nodes in the binary tree without recursion
# time complexity O(n)

def sumOfBinaryTreeWithoutRecursion(root):
    if root is None:
        return 0
    sum = 0
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        root = q.get()
        sum += root.data
        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)
    return sum

# give an algorithm for converting a tree to its mirror

def mirror(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)
    return root

# give an algorithm for checking if a tree is mirror of another tree

def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)  
    
                                                         

def test():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    
    print(mirror(root))

if __name__ == '__main__':
    test()          
    