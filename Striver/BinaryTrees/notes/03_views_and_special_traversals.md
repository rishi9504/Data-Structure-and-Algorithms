# Views and Special Traversals

Source pages: 12-18 of the handwritten PDF.

## Zigzag / Spiral Traversal

### Core Intuition

This is level order traversal where every alternate level is read in the opposite direction.

The notes include two approaches:

- place values using a deque/index based on the current direction
- easier revision approach: collect the level normally, reverse the level when direction is right-to-left

### Algorithm

1. Do BFS level by level.
2. Maintain a `left_to_right` flag.
3. Reverse the level list when the flag is false.
4. Flip the flag after each level.

### Complexity

Time: O(N)  
Space: O(W)

### Related Problem

LeetCode 103 - Binary Tree Zigzag Level Order Traversal

## Boundary Traversal

### Core Intuition

The boundary is the outside line of the tree. For anti-clockwise traversal:

`root -> left boundary -> leaves -> reversed right boundary`

Leaves are handled separately so they are not duplicated.

### Algorithm

1. Add root if it is not a leaf.
2. Walk down the left boundary, preferring left child, otherwise right child.
3. Add all leaf nodes using DFS.
4. Walk down the right boundary, preferring right child, otherwise left child.
5. Reverse the collected right boundary and append it.

### Important Detail / Common Mistake

Do not add leaf nodes while collecting left/right boundary, because the leaf pass will add them.

### Related Problem

No direct LeetCode mapping confirmed. Commonly asked as GFG boundary traversal.

## Vertical Order Traversal

### Core Intuition

Give every node coordinates:

- left child: column `-1`, row `+1`
- right child: column `+1`, row `+1`
- down one level: row `+1`

Collect `(column, row, value)`, sort, then group by column.

### Important Detail / Common Mistake

The handwritten note calls out that Python tuple sorting helps here: sorting `(col, row, value)` automatically sorts by column first, then row, then value.

### Complexity

Time: O(N log N)  
Space: O(N)

### Related Problem

LeetCode 987 - Vertical Order Traversal of a Binary Tree

## Top View

### Core Intuition

Use BFS with vertical columns. For top view, only store the first node seen in each column.

### Why It Works

BFS sees upper levels before lower levels. So the first node encountered for a column is the visible node from the top.

### What I Should Remember

If a column is seen for the first time, store it. If it already exists, skip it.

### Related Problem

No direct LeetCode mapping confirmed.

## Bottom View

### Core Intuition

Use BFS with vertical columns. For bottom view, keep overwriting the value for a column.

### Why It Works

Later BFS visits represent nodes that are lower or later in the same vertical line. The last stored value becomes the bottom visible node.

### Important Detail / Common Mistake

The notes mark that when nodes overlap at the same column/level, the later/right-side node remains because it overwrites the earlier one.

### Related Problem

No direct LeetCode mapping confirmed.

## Left and Right View

### Core Intuition

A side view contains one node per level.

- Right view: first node seen when DFS visits right before left.
- Left view: first node seen when DFS visits left before right.

### Algorithm

1. DFS with `level`.
2. If `level == len(result)`, this is the first node seen at that level.
3. Add it to the result.
4. Visit the preferred side first.

### Related Problem

LeetCode 199 - Binary Tree Right Side View
