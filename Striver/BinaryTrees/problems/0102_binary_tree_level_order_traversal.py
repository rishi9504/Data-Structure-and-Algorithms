"""
LeetCode 102 - Binary Tree Level Order Traversal

Pattern:
BFS

Key idea:
Use a queue to process the tree level by level.

Time: O(N)
Space: O(W)
"""

from __future__ import annotations

from collections import deque
from typing import Deque, List, Optional


class Solution:
    def levelOrder(self, root: Optional["TreeNode"]) -> List[List[int]]:
        if root is None:
            return []

        result: List[List[int]] = []
        queue: Deque["TreeNode"] = deque([root])

        while queue:
            level: List[int] = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result
