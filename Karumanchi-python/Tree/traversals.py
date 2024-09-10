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

