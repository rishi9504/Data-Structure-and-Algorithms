"""
LeetCode 100 - Same Tree

Pattern:
DFS

Key idea:
Both structure and values must match.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def isSameTree(
        self,
        p: Optional["TreeNode"],
        q: Optional["TreeNode"],
    ) -> bool:
        if p is None or q is None:
            return p is q

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
