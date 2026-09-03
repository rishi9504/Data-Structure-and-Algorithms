"""
LeetCode 105 - Construct Binary Tree from Preorder and Inorder

Pattern:
Tree construction

Key idea:
Preorder gives root; inorder gives left/right split.

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index: Dict[int, int] = {
            value: index for index, value in enumerate(inorder)
        }
        preorder_index = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)
            mid = inorder_index[root_value]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
