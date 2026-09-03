"""
Top View of Binary Tree

Pattern:
BFS + vertical index

Key idea:
For each column, keep only the first node seen by BFS.

Time: O(N log N)
Space: O(N)
"""

from __future__ import annotations

from collections import deque
from typing import Deque, Dict, List, Optional


def top_view(root: Optional["TreeNode"]) -> List[int]:
    if root is None:
        return []

    view: Dict[int, int] = {}
    queue: Deque[tuple["TreeNode", int]] = deque([(root, 0)])

    while queue:
        node, col = queue.popleft()
        if col not in view:
            view[col] = node.val

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    return [view[col] for col in sorted(view)]
