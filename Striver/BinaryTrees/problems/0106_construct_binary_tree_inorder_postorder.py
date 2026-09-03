"""
LeetCode 106 - Construct Binary Tree from Inorder and Postorder

Pattern:
Tree construction

Key idea:
Postorder gives root from the end; build right subtree first.

Time: O(N)
Space: O(N)
"""

from __future__ import annotations

from typing import Dict, List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index: Dict[int, int] = {
            value: index for index, value in enumerate(inorder)
        }
        postorder_index = len(postorder) - 1

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal postorder_index
            if left > right:
                return None

            root_value = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_value)
            mid = inorder_index[root_value]
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            return root

        return build(0, len(inorder) - 1)
