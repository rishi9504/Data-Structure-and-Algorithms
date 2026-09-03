"""
Morris Inorder Traversal

Pattern:
Threaded binary tree

Key idea:
Create a temporary return path from predecessor back to current.

Time: O(N)
Space: O(1)
"""

from __future__ import annotations

from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        result: List[int] = []
        current = root

        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right is not current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right

        return result
