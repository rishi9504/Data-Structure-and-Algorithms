"""
Root to Node Path

Pattern:
DFS + backtracking

Key idea:
Append while exploring, pop when a branch fails.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import List, Optional


def root_to_node_path(root: Optional["TreeNode"], target: int) -> List[int]:
    path: List[int] = []

    def dfs(node: Optional["TreeNode"]) -> bool:
        if node is None:
            return False

        path.append(node.val)
        if node.val == target:
            return True

        if dfs(node.left) or dfs(node.right):
            return True

        path.pop()
        return False

    return path if dfs(root) else []
