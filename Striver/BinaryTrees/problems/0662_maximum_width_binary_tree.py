"""
LeetCode 662 - Maximum Width of Binary Tree

Pattern:
BFS + positional indexing

Key idea:
Assign complete-tree indexes and normalize each level.

Time: O(N)
Space: O(W)
"""

from __future__ import annotations

from collections import deque
from typing import Deque, Optional


class Solution:
    def widthOfBinaryTree(self, root: Optional["TreeNode"]) -> int:
        if root is None:
            return 0

        max_width = 0
        queue: Deque[tuple["TreeNode", int]] = deque([(root, 0)])

        while queue:
            level_size = len(queue)
            min_index = queue[0][1]
            first = last = 0

            for i in range(level_size):
                node, index = queue.popleft()
                index -= min_index

                if i == 0:
                    first = index
                if i == level_size - 1:
                    last = index

                if node.left:
                    queue.append((node.left, 2 * index + 1))
                if node.right:
                    queue.append((node.right, 2 * index + 2))

            max_width = max(max_width, last - first + 1)

        return max_width
