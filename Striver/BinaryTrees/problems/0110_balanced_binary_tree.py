"""
LeetCode 110 - Balanced Binary Tree

Pattern:
DFS + sentinel height

Key idea:
Return -1 as soon as any subtree is unbalanced.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional["TreeNode"]) -> bool:
        def height(node: Optional["TreeNode"]) -> int:
            if node is None:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1
