"""
LeetCode 543 - Diameter of Binary Tree

Pattern:
Postorder DFS

Key idea:
At each node, candidate diameter is left height + right height.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional["TreeNode"]) -> int:
        diameter = 0

        def height(node: Optional["TreeNode"]) -> int:
            nonlocal diameter
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        height(root)
        return diameter
