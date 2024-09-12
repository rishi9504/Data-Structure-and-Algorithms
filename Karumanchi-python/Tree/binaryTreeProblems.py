# give an algorithm for finding maximum element in binary tree
# time complexity O(n)
import queue
from binaryTree import BinaryTreeNode


maxData = float('-inf')
def findMax(root):
    global maxData
    if root is None:
        return
    if root.data > maxData:
        maxData = root.data
    findMax(root.left)
    findMax(root.right)
    return maxData

# give an algorithm for finding maximum element in binary tree without recursion
# time complexity O(n)

def findMaxWithoutRecursion(root):
    if root is None:
        return
    maxData = float('-inf')
    while root is not None:
        if root.data > maxData:
            maxData = root.data
        root = root.right
    return maxData  

# give an algorithm for finding maximum element in binary tree without recursion using queue
# time complexity O(n)

def findMaxWithoutRecursionUsingQueue(root):
    if root is None:
        return
    maxData = float('-inf')
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        root = q.get()
        if root.data > maxData:
            maxData = root.data
        if root.left is not None:
            q.put(root.left)
        if root.right is not None:
            q.put(root.right)
    return maxData

# give an algorithm for finding maximum element in binary tree without recursion using stack
# time complexity O(n)

def findMaxWithoutRecursionUsingStack(root):
    if root is None:
        return
    maxData = float('-inf')
    s = []
    s.append(root)
    while s:
        root = s.pop()
        if root.data > maxData:
            maxData = root.data
        if root.right is not None:
            s.append(root.right)
        if root.left is not None:
            s.append(root.left)
    return maxData

# give an algorithm for searching element in binary tree
# time complexity O(n)

def findRecursive(root, data):
    if root is None:
        return False
    if root.data == data:
        return True
    return findRecursive(root.left, data) or findRecursive(root.right, data)


# give an algorithm for searching element in binary tree without recursion
# time complexity O(n)

def findWithoutRecursion(root, data):
    if root is None:
        return False
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        root = q.get()
        if root.data == data:
            return True
        if root.left is not None:
            q.put(root.left)
        if root.right is not None:
            q.put(root.right)
    return False


# give an algorithm for finding the size of the binary tree
# time complexity O(n)

def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)

# give an algorithm for finding the size of the binary tree without recursion
# time complexity O(n)

def sizeWithoutRecursion(root):
    if root is None:
        return 0
    s = 0
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        root = q.get()
        s += 1
        if root.left is not None:
            q.put(root.left)
        if root.right is not None:
            q.put(root.right)
    return s

# give an algorithm for finding the height of the binary tree
# time complexity O(n)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# give an algorithm for finding the height of the binary tree without recursion
# time complexity O(n)  

def heightWithoutRecursion(root):
    if root is None:
        return 0
    h = 0
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        root = q.get()
        h += 1
        if root.left is not None:
            q.put(root.left)
        if root.right is not None:
            q.put(root.right)
    return h

# give an algorithm to find the deepest node of the binary tree

def deepestNode(root):
    if root is None:
        return None
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        root = q.get()
        if root.left is not None:
            q.put(root.left)
        if root.right is not None:
            q.put(root.right)
    return root

# give an algorithm for finding the number of leaf nodes in the binary tree without recursion

def numberOfLeafNodes(root):
    if root is None:
        return 0
    q = queue.Queue()
    q.put(root)
    count = 0
    while not q.empty():
        root = q.get()
        if root.left is None and root.right is None:
            count += 1
        if root.left is not None:
            q.put(root.left)
        if root.right is not None:
            q.put(root.right)
    return count

# give an algorithm for finding the number of full nodes in the binary tree without recursion

def numberOfFullNodes(root):
    if root is None:
        return 0
    q = queue.Queue()
    q.put(root)
    count = 0
    while not q.empty():
        root = q.get()
        if root.left is not None and root.right is not None:
            count += 1
        if root.left is not None:
            q.put(root.left)
        if root.right is not None:
            q.put(root.right)
    return count

# give an algorithm for finding the number of half nodes in the binary tree without recursion

def numberOfHalfNodes(root):
    if root is None:
        return 0
    q = queue.Queue()
    q.put(root)
    count = 0
    while not q.empty():
        root = q.get()
        if (root.left is not None and root.right is None) or (root.left is None and root.right is not None):
            count += 1
        if root.left is not None:
            q.put(root.left)
        if root.right is not None:
            q.put(root.right)
    return count

# given two binary trees, return true if they are structurally identical
# 

def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data != root2.data:
        return False
    return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)    

# give an algorithm for finding the diameter of a binary tree. The diameter is defined as the number of nodes
# that are on the longest path between two end nodes in the tree. 
ptr = 0
def diameterOfTree(root):
    global ptr
    if root is None:
        return 0
    left = diameterOfTree(root.left)
    right = diameterOfTree(root.right)
    if (left+right)>ptr:
        ptr = left+right
    # ptr = max(ptr, 1 + left + right)

    return 1 + max(left, right)

# optional code for diameter of a tree

def diameterOptional(root):
    if root is None:
        return 0
    lHeight = height(root.left)
    rHeight = height(root.right)
    lDiameter = diameterOptional(root.left)
    rDiameter = diameterOptional(root.right)
    return max(lHeight+rHeight+1, max(lDiameter, rDiameter))

# give an algorithm for finding the level that has the maximum sum in the binary tree

def levelWithMaxSum(root):
    if root is None:
        return 0
    q = queue.Queue()
    q.put(root)
    level = 0
    maxSum = -float('inf')
    while not q.empty():
        level += 1
        count = q.qsize()
        levelSum = 0
        while count > 0:
            root = q.get()
            levelSum += root.data
            if root.left is not None:
                q.put(root.left)
            if root.right is not None:
                q.put(root.right)
            count -= 1
        if levelSum > maxSum:
            maxSum = levelSum
            maxLevel = level
    return maxLevel


# given a binary tree, print out all its root-to-leaf paths

# both pathsappender and printpaths are used to achieve the issue solution

def pathsAppender(root, path, paths):
    if root is None:
        return 0
    path.append(root.data)
    if root.left is None and root.right is None:
        paths.append(path[:])
    else:
        pathsAppender(root.left, path, paths)
        pathsAppender(root.right, path, paths)
    path.pop()

def printPaths(root):
    paths = []
    path = []
    pathsAppender(root, path, paths)
    return paths


# given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number
# find the total sum of all root-to-leaf numbers

def sumNumbers(root):
    if root is None:
        return 0
    currentSum = 0
    sum =[0]
    sumNumbersAppender(root, currentSum, sum)
    return sum[0]

def sumNumbersAppender(root, currentSum, sum):
    if root is None:
        return
    currentSum = currentSum*10 + root.data
    if root.left is None and root.right is None:
        sum[0] += currentSum
        return
    else:
        sumNumbersAppender(root.left, currentSum, sum)
        sumNumbersAppender(root.right, currentSum, sum)



# given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.













def test():
    root1 = BinaryTreeNode(1)
    root1.left = BinaryTreeNode(2)
    root1.right = BinaryTreeNode(3)
    root1.left.left = BinaryTreeNode(4)
    root1.left.right = BinaryTreeNode(5)
    root1.right.left = BinaryTreeNode(6)
    root1.right.right = BinaryTreeNode(7)

    root2 = BinaryTreeNode(1)
    root2.left = BinaryTreeNode(2)
    root2.right = BinaryTreeNode(3)
    root2.left.left = BinaryTreeNode(4)
    root2.left.right = BinaryTreeNode(5)
    root2.right.left = BinaryTreeNode(6)
    root2.right.right = BinaryTreeNode(7)

    # change the method name here to test other functions
    print(sumNumbers(root1))

if __name__ == '__main__':
    test()      