"""
LeetCode 145 - Binary Tree Postorder Traversal

Pattern:
DFS

Key idea:
Process left and right subtrees before the root.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        result: List[int] = []

        def dfs(node: Optional["TreeNode"]) -> None:
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result

    def postorderTraversalIterative(self, root: Optional["TreeNode"]) -> List[int]:
        if root is None:
            return []

        result: List[int] = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
