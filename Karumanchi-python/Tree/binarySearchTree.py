# Define the Node class to represent each node in the tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Define the Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new key into the BST
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    # Recursive helper function to insert a new key
    def _insert_rec(self, root, key):
        # Check if the key to insert is less than the current node's key
        if key < root.key:
            # If the left child is None, insert the new key here
            if root.left is None:
                root.left = Node(key)
            else:
                # Otherwise, recursively call the function on the left child
                self._insert_rec(root.left, key)
        # Check if the key to insert is greater than the current node's key
        elif key > root.key:
            # If the right child is None, insert the new key here
            if root.right is None:
                root.right = Node(key)
            else:
                # Otherwise, recursively call the function on the right child
                self._insert_rec(root.right, key)

    # Delete a key from the BST
    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    # Recursive helper function to delete a key
    def _delete_rec(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_rec(root.left, key)
        elif key > root.key:
            root.right = self._delete_rec(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.key = self._min_value(root.right)
            root.right = self._delete_rec(root.right, root.key)

        return root

    # Helper function to find the minimum value node in the subtree
    def _min_value(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    # Inorder traversal of the tree
    def inorder(self):
        self._inorder_rec(self.root)
        print()  # for a newline after traversal

    # Recursive helper function for inorder traversal
    def _inorder_rec(self, root):
        if root is not None:
            self._inorder_rec(root.left)
            print(root.key, end=" ")
            self._inorder_rec(root.right)


# Main method to test the BST implementation
if __name__ == "__main__":
    tree = BinarySearchTree()

    # Create the tree by inserting nodes
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print("Inorder traversal of the given tree:")
    tree.inorder()

    # Delete a node with key 20
    print("\nDelete 20")
    tree.delete(20)
    print("Inorder traversal of the modified tree:")
    tree.inorder()

    # Delete a node with key 30
    print("\nDelete 30")
    tree.delete(30)
    print("Inorder traversal of the modified tree:")
    tree.inorder()

    # Delete a node with key 50
    print("\nDelete 50")
    tree.delete(50)
    print("Inorder traversal of the modified tree:")
    tree.inorder()
