# Basics and Traversals

Source pages: 1-6 of the handwritten PDF.

## Binary Tree Terminology

A binary tree is a hierarchical data structure. The top node is the root. Nodes below another node are its children. A leaf node does not have children.

A subtree is a specific section of a tree. Ancestors are all the parents on the path above a node.

## Types of Binary Trees

- Full binary tree: every node has either 0 or 2 children.
- Complete binary tree: all levels are completely filled except possibly the last, and the last level is filled as left as possible.
- Perfect binary tree: all leaf nodes are at the same level.
- Balanced binary tree: height is controlled, roughly at most `log(n)` for `n` nodes.
- Degenerate tree: skew tree, behaving like a linked list.

### What I Should Remember

For interviews, identify the tree shape first. A complete tree gives indexing/counting shortcuts, while a skew tree is the recursion worst case.

## Binary Tree Representation in Python

The handwritten node model was:

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
```

Most LeetCode versions use `node.val` instead of `node.value`.

## DFS vs BFS

BFS is level order traversal: print level by level and use a queue.

DFS goes deep before moving across the level. The three main DFS orders are:

- Inorder: left, root, right
- Preorder: root, left, right
- Postorder: left, right, root

## Preorder Traversal

### Core Intuition

Visit the root before both subtrees.

### Algorithm

1. If the node is `None`, return.
2. Visit / append the current node.
3. Traverse left.
4. Traverse right.

### Complexity

Time: O(N)  
Space: O(H)

### Related Problem

LeetCode 144 - Binary Tree Preorder Traversal

## Inorder Traversal

### Core Intuition

Visit the left subtree first, then root, then right subtree.

### Algorithm

1. If the node is `None`, return.
2. Traverse left.
3. Visit / append the current node.
4. Traverse right.

### Complexity

Time: O(N)  
Space: O(H)

### Related Problem

LeetCode 94 - Binary Tree Inorder Traversal

## Postorder Traversal

### Core Intuition

Process both children before processing the current node. This is useful when the answer for a node depends on completed answers from its subtrees.

### Algorithm

1. If the node is `None`, return.
2. Traverse left.
3. Traverse right.
4. Visit / append the current node.

### Complexity

Time: O(N)  
Space: O(H)

### Related Problem

LeetCode 145 - Binary Tree Postorder Traversal

## Level Order Traversal

### Core Intuition

Use a queue because BFS must finish the current level before going deeper.

### Algorithm

1. Push the root into the queue.
2. While the queue is not empty, pop the front node.
3. Add its value to the current answer.
4. Push left child, then right child, when they exist.

### Complexity

Time: O(N)  
Space: O(W), where `W` is the maximum width of the tree.

### Related Problem

LeetCode 102 - Binary Tree Level Order Traversal
