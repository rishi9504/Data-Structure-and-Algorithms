"""
LeetCode 101 - Symmetric Tree

Pattern:
Mirror DFS

Key idea:
Compare outside pairs and inside pairs.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional["TreeNode"]) -> bool:
        if root is None:
            return True

        def mirror(left: Optional["TreeNode"], right: Optional["TreeNode"]) -> bool:
            if left is None or right is None:
                return left is right

            return (
                left.val == right.val
                and mirror(left.left, right.right)
                and mirror(left.right, right.left)
            )

        return mirror(root.left, root.right)
