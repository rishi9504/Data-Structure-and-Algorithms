"""
Left View of Binary Tree

Pattern:
DFS + level

Key idea:
Visit left first and take the first node seen at each level.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import List, Optional


def left_view(root: Optional["TreeNode"]) -> List[int]:
    result: List[int] = []

    def dfs(node: Optional["TreeNode"], level: int) -> None:
        if node is None:
            return

        if level == len(result):
            result.append(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result
