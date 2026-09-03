"""
LeetCode 124 - Binary Tree Maximum Path Sum

Pattern:
Tree DP

Key idea:
Update answer with both sides, but return only one extendable side.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional["TreeNode"]) -> int:
        best = float("-inf")

        def gain(node: Optional["TreeNode"]) -> int:
            nonlocal best
            if node is None:
                return 0

            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)

            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return int(best)
