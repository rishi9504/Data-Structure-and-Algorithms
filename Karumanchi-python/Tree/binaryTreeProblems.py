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

def test():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    # change the method name here to test other functions
    print(numberOfHalfNodes(root))

if __name__ == '__main__':
    test()      