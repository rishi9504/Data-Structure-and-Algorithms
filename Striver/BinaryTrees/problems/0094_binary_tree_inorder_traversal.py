"""
LeetCode 94 - Binary Tree Inorder Traversal

Pattern:
DFS

Key idea:
Visit left subtree, then root, then right subtree.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        result: List[int] = []

        def dfs(node: Optional["TreeNode"]) -> None:
            if node is None:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result

    def inorderTraversalIterative(self, root: Optional["TreeNode"]) -> List[int]:
        result: List[int] = []
        stack: List["TreeNode"] = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
