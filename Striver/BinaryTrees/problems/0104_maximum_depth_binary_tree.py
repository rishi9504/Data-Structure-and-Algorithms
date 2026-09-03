"""
LeetCode 104 - Maximum Depth of Binary Tree

Pattern:
DFS

Key idea:
Depth is 1 plus the maximum depth of the two subtrees.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def maxDepth(self, root: Optional["TreeNode"]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def heightInEdges(self, root: Optional["TreeNode"]) -> int:
        if root is None:
            return -1
        return 1 + max(self.heightInEdges(root.left), self.heightInEdges(root.right))
