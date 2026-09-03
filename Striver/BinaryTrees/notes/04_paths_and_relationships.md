# Paths and Relationships

Source pages: 20-21 of the handwritten PDF.

## Root-to-Node Path

### Core Intuition

Use traversal plus backtracking. The path list represents the current route from root to the node being explored.

If the target is found, return `True` and keep the path. If a branch fails, pop the node before returning.

### Algorithm

1. Add current node to `path`.
2. If current node is the target, return `True`.
3. Search left or right.
4. If either side succeeds, keep the path and return `True`.
5. If both fail, pop current node and return `False`.

### Important Detail / Common Mistake

The handwritten note explicitly says: when a branch fails, come back and go to the other side, so the current failed node must be removed from the path.

### Related Problem

No direct LeetCode mapping confirmed. Commonly asked as root-to-node path.

## Lowest Common Ancestor

### Core Intuition

The root-to-node path idea says: the LCA is the last common node in both target paths.

The recursive Striver version asks a relationship question instead: which branch contains my targets?

### Algorithm

1. If `root` is `None`, return `None`.
2. If `root` is `p` or `q`, return `root`.
3. Search left and right.
4. If both sides return a node, current root is the LCA.
5. If only one side returns a node, bubble that node upward.

### Why It Works

When the two target nodes split into different branches, the current root is the lowest place where both branches meet.

### Related Problem

LeetCode 236 - Lowest Common Ancestor of a Binary Tree
