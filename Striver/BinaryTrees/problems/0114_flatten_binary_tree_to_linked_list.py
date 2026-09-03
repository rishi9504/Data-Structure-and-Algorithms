"""
LeetCode 114 - Flatten Binary Tree to Linked List

Pattern:
Morris-style rewiring

Key idea:
Attach original right subtree to the predecessor of the left subtree.

Time: O(N)
Space: O(1)
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def flatten(self, root: Optional["TreeNode"]) -> None:
        current = root

        while current:
            if current.left:
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = current.right
                current.right = current.left
                current.left = None

            current = current.right
