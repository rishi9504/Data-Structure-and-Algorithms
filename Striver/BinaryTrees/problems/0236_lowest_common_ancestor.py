"""
LeetCode 236 - Lowest Common Ancestor of a Binary Tree

Pattern:
Recursive relationship

Key idea:
If targets split across left and right, current node is the LCA.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional["TreeNode"],
        p: "TreeNode",
        q: "TreeNode",
    ) -> Optional["TreeNode"]:
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right
