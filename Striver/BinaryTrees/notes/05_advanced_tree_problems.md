# Advanced Tree Problems

Source pages: 22-27 of the handwritten PDF.

## Maximum Width of Binary Tree

### Core Intuition

Index the tree as if it were a complete binary tree:

- 0-based left child: `2 * i + 1`
- 0-based right child: `2 * i + 2`

For each level:

`width = last_index - first_index + 1`

### Important Detail / Common Mistake

Indexes can become very large in a deep tree, so normalize each level by subtracting the first index of that level.

### Related Problem

LeetCode 662 - Maximum Width of Binary Tree

## Children Sum Property

### Core Intuition

For every node:

`node value = left child value + right child value`

To make the property true, we can increment node/child values. We never reduce a value.

### Algorithm

Check version:

1. A leaf already satisfies the property.
2. Compute existing child sum.
3. Compare it with the current node.
4. Recursively validate left and right.

Mutation version:

1. If child sum is greater than the node, update the node.
2. Otherwise push the node value down to existing children.
3. Recurse on children.
4. On the way back, set the node to the new sum of its children.

### Related Problem

No direct LeetCode mapping confirmed. Commonly asked as GFG children sum property.

## Nodes at Distance K

### Core Intuition

Normally a tree only lets us move down to children. For distance K, we may need to move up to the parent too.

So treat the tree like an undirected graph:

`left child, right child, parent`

### Algorithm

1. Build a parent map using BFS.
2. Start BFS from the target node.
3. Use visited set to avoid going in circles.
4. Expand level by level until distance `K`.
5. Return all nodes left in the queue.

### What I Should Remember

Parent is just another neighbour.

### Related Problem

LeetCode 863 - All Nodes Distance K in Binary Tree

## Burning Tree

### Core Intuition

This is the same idea as Distance K, but instead of stopping at K, continue BFS until no more nodes can burn.

Each BFS level is one unit of time.

### Algorithm

1. Build the parent map.
2. Start from the target.
3. Burn left, right, and parent if not visited.
4. Increase time only if at least one new node burns during that BFS layer.

### Related Problem

No direct LeetCode mapping confirmed. Commonly asked as GFG burning tree.

## Count Nodes in a Complete Binary Tree

### Core Intuition

In a complete binary tree, if the leftmost height equals the rightmost height, that subtree is perfect.

A perfect binary tree with height `h` has:

`2^h - 1` nodes

### Algorithm

1. Compute the leftmost height.
2. Compute the rightmost height.
3. If equal, return `(1 << height) - 1`.
4. Otherwise return `1 + count(left) + count(right)`.

### Important Detail / Common Mistake

Only complete trees allow this shortcut. For arbitrary binary trees, use normal O(N) traversal.

### Related Problem

LeetCode 222 - Count Complete Tree Nodes
