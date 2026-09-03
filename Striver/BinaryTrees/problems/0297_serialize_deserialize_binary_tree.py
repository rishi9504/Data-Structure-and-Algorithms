"""
LeetCode 297 - Serialize and Deserialize Binary Tree

Pattern:
Serialization

Key idea:
Use level order with # markers for missing children.

Time: O(N)
Space: O(N)
"""

from __future__ import annotations

from collections import deque
from typing import Deque, Optional


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


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        values = []
        queue: Deque[Optional[TreeNode]] = deque([root])

        while queue:
            node = queue.popleft()
            if node is None:
                values.append("#")
                continue

            values.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(",")
        if values[0] == "#":
            return None

        root = TreeNode(int(values[0]))
        queue: Deque[TreeNode] = deque([root])
        index = 1

        while queue and index < len(values):
            node = queue.popleft()

            if index < len(values) and values[index] != "#":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1

            if index < len(values) and values[index] != "#":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root
