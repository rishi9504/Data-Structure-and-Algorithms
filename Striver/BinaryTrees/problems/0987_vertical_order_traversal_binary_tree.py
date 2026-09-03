"""
LeetCode 987 - Vertical Order Traversal of a Binary Tree

Pattern:
DFS + vertical index

Key idea:
Collect (column, row, value), sort, then group by column.

Time: O(N log N)
Space: O(N)
"""

from __future__ import annotations

from typing import List, Optional, Tuple


class Solution:
    def verticalTraversal(self, root: Optional["TreeNode"]) -> List[List[int]]:
        nodes: List[Tuple[int, int, int]] = []

        def dfs(node: Optional["TreeNode"], row: int, col: int) -> None:
            if node is None:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()

        result: List[List[int]] = []
        previous_col = None
        for col, _row, value in nodes:
            if col != previous_col:
                result.append([])
                previous_col = col
            result[-1].append(value)

        return result
