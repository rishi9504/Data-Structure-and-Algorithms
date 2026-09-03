# Construction, Serialization and Morris

Source pages: 28-33 of the handwritten PDF.

## Construct Binary Tree from Preorder + Inorder

### Core Intuition

Preorder gives the root first:

`root, left, right`

Inorder tells how to split:

`left, root, right`

### Algorithm

1. Take the next preorder value as root.
2. Find that root in inorder.
3. Build left subtree from the left inorder range.
4. Build right subtree from the right inorder range.

### Important Detail / Common Mistake

Use a hashmap from value to inorder index so the split is O(1).

### Related Problem

LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal

## Construct Binary Tree from Postorder + Inorder

### Core Intuition

Postorder gives the root at the end:

`left, right, root`

Inorder still gives the split point.

### Algorithm

1. Take the current value from the end of postorder as root.
2. Split inorder using the root value.
3. Build right subtree first.
4. Build left subtree after that.

### Important Detail / Common Mistake

Build right first because consuming postorder from the end sees `root`, then right-side values, then left-side values.

### Related Problem

LeetCode 106 - Construct Binary Tree from Inorder and Postorder Traversal

## Serialize and Deserialize Binary Tree

### Core Intuition

Convert root to string and string back to root.

The notes use level order traversal with `#` for `None`, so structure is preserved.

### Algorithm

Serialize:

1. BFS from root.
2. Append node values.
3. Append `#` for null children.

Deserialize:

1. Split the data string.
2. Create root from the first value.
3. Use a queue to assign left and right children in order.
4. Skip children where the value is `#`.

### Related Problem

LeetCode 297 - Serialize and Deserialize Binary Tree

## Morris Traversal

### Core Intuition

Morris traversal creates a temporary return path so inorder traversal can run without recursion or stack.

For a node with a left child:

1. Find the rightmost node in the left subtree.
2. If no thread exists, point that predecessor's right to current and move left.
3. If the thread already exists, remove it, visit current, and move right.

### What I Should Remember

The temporary thread replaces the recursion stack's return path.

### Related Problem

LeetCode 94 technique - Binary Tree Inorder Traversal using O(1) extra space.

## Flatten Binary Tree to Linked List

### Core Intuition

Use the Morris-style predecessor idea to rearrange the tree in place into a right-only linked list following preorder traversal.

### Algorithm

1. Start at current node.
2. If current has a left subtree, find the rightmost node of that left subtree.
3. Attach current's original right subtree to that predecessor.
4. Move left subtree to the right.
5. Set current left to `None`.
6. Move current to current.right.

### Related Problem

LeetCode 114 - Flatten Binary Tree to Linked List
