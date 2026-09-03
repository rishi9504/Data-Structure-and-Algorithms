# Tree Properties

Source pages: 7-11 and 19 of the handwritten PDF.

## Maximum Depth / Height

### Core Intuition

Height is the longest downward distance from the root to the deepest node.

The handwritten note defines height as number of edges, so an empty tree returns `-1`. LeetCode 104 usually asks for maximum depth in nodes, so an empty tree returns `0`.

### Algorithm

1. If root is `None`, return the base height.
2. Recursively get left height.
3. Recursively get right height.
4. Return `1 + max(left_height, right_height)`.

### Complexity

Time: O(N)  
Space: O(H)

### Related Problem

LeetCode 104 - Maximum Depth of Binary Tree

## Balanced Binary Tree

### Core Intuition

For every node, `height(left) - height(right)` must be at most `1` in absolute value.

### Algorithm

Use a bottom-up height function. If any subtree is already unbalanced, return `-1` upward as a failure signal.

### Why It Works

Each node receives the height of both subtrees only after those subtrees have been checked. The `-1` sentinel avoids recomputing heights repeatedly.

### Complexity

Time: O(N)  
Space: O(H)

### Related Problem

LeetCode 110 - Balanced Binary Tree

## Diameter of Binary Tree

### Core Intuition

Diameter is the longest path between two nodes. The path does not need to pass through the root.

For each node, ask: what is the longest path passing through this node? That is `left_height + right_height`.

### Algorithm

1. Run postorder DFS.
2. Get left and right heights.
3. Update a global/nonlocal maximum with `left + right`.
4. Return `1 + max(left, right)` as this node's height.

### Complexity

Time: O(N)  
Space: O(H)

### Related Problem

LeetCode 543 - Diameter of Binary Tree

## Maximum Path Sum

### Core Intuition

Think of a path from node A to node B. At each node, the best path using that node as the highest connection is:

`node.val + best_left_gain + best_right_gain`

Negative branches are ignored because they reduce the sum.

### Algorithm

1. DFS returns the best one-side gain that can continue to the parent.
2. Clamp child gains with `max(child_gain, 0)`.
3. Update the answer with `node.val + left_gain + right_gain`.
4. Return `node.val + max(left_gain, right_gain)`.

### Important Detail / Common Mistake

The value used to update the global answer may use both sides, but the value returned to the parent can use only one side.

### Related Problem

LeetCode 124 - Binary Tree Maximum Path Sum

## Identical Binary Trees

### Core Intuition

Two trees are identical only when both structure and node values match.

### Algorithm

1. If both nodes are `None`, return `True`.
2. If only one is `None`, return `False`.
3. Compare current values.
4. Recursively compare left with left and right with right.

### Related Problem

LeetCode 100 - Same Tree

## Symmetric Binary Tree

### Core Intuition

Check whether the tree forms a mirror of itself around the center.

For every mirror pair:

- values must be equal
- left's left must match right's right
- left's right must match right's left

### Algorithm

Run a helper `mirror(left, right)` from `root.left` and `root.right`.

### Complexity

Time: O(N)  
Space: O(H)

### Related Problem

LeetCode 101 - Symmetric Tree
