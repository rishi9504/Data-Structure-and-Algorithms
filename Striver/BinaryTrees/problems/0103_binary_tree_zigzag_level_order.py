"""
LeetCode 103 - Binary Tree Zigzag Level Order Traversal

Pattern:
BFS + direction flag

Key idea:
Collect each level and reverse alternate levels.

Time: O(N)
Space: O(W)
"""

from __future__ import annotations

from collections import deque
from typing import Deque, List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional["TreeNode"]) -> List[List[int]]:
        if root is None:
            return []

        result: List[List[int]] = []
        queue: Deque["TreeNode"] = deque([root])
        left_to_right = True

        while queue:
            level: List[int] = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right

        return result
