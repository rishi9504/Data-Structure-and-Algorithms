
from collections import deque
from binaryTree import BinaryTreeNode

# Preorder Traversal
# Visit the root node first
# Then visit the left subtree
# Then visit the right subtree
def preOrderRecusrsive(root):
    if root:
        print(root.data)
        preOrderRecusrsive(root.left)
        preOrderRecusrsive(root.right)

def preOrderIterative(root):
    if root:
        stack = [root]
        while stack:
            root = stack.pop()
            print(root.data)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

# inorder traversal
# Visit the left subtree
# Then visit the root node
# Then visit the right subtree

def inOrderRecusrsive(root):
    if root:
        inOrderRecusrsive(root.left)
        print(root.data)
        inOrderRecusrsive(root.right)

def inOrderIterative(root):
    if root:
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                print(root.data)
                root = root.right


# postorder traversal
# Visit the left subtree
# Then visit the right subtree
# Then visit the root node

def postOrderRecusrsive(root):
    if root:
        postOrderRecusrsive(root.left)
        postOrderRecusrsive(root.right)
        print(root.data)

def postOrderIterative(root):
    if root:
        stack = [root]
        while stack:
            root = stack.pop()
            print(root.data)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)



# level order traversal


import queue
def levelOrder(root):
    if root:
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            root = q.get()
            print(root.data)
            if root.left:
                q.put(root.left)
            if root.right:
                q.put(root.right)

# give an algorithm for printing the level order data in reverse order

def levelOrderTraversalInReverse(root):
    q = deque()
    q.append(root)
    ans = deque()
    while q:
        node = q.popleft()
        if node is None:
            continue

        ans.appendleft(node.data)

        if node.right:
            q.append(node.right)

        if node.left:
            q.append(node.left)

    return ans

def test():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    
    print("level order traversal")
    levelOrder(root)


if __name__ == '__main__':
    test()  


