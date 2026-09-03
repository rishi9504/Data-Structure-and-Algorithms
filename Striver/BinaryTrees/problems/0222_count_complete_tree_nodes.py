"""
LeetCode 222 - Count Complete Tree Nodes

Pattern:
Complete tree height check

Key idea:
If leftmost and rightmost heights match, subtree is perfect.

Time: O(log^2 N)
Space: O(log N)
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def countNodes(self, root: Optional["TreeNode"]) -> int:
        if root is None:
            return 0

        left_height = self._left_height(root)
        right_height = self._right_height(root)

        if left_height == right_height:
            return (1 << left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def _left_height(self, node: Optional["TreeNode"]) -> int:
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def _right_height(self, node: Optional["TreeNode"]) -> int:
        height = 0
        while node:
            height += 1
            node = node.right
        return height
