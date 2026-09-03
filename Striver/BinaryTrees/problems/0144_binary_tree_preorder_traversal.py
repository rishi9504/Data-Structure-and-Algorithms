"""
LeetCode 144 - Binary Tree Preorder Traversal

Pattern:
DFS

Key idea:
Visit root first, then left subtree, then right subtree.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        result: List[int] = []

        def dfs(node: Optional["TreeNode"]) -> None:
            if node is None:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

    def preorderTraversalIterative(self, root: Optional["TreeNode"]) -> List[int]:
        if root is None:
            return []

        result: List[int] = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
