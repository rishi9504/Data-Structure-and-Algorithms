"""
Burning Tree

Pattern:
Parent map + BFS

Key idea:
Same as Distance K, but BFS continues until no node is left.

Time: O(N)
Space: O(N)
"""

from __future__ import annotations

from collections import deque
from typing import Deque, Dict, Optional, Set


def min_time_to_burn(root: Optional["TreeNode"], target_value: int) -> int:
    if root is None:
        return 0

    parent: Dict["TreeNode", "TreeNode"] = {}
    target = None
    queue: Deque["TreeNode"] = deque([root])

    while queue:
        node = queue.popleft()
        if node.val == target_value:
            target = node

        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    if target is None:
        return 0

    visited: Set["TreeNode"] = {target}
    queue = deque([target])
    time = 0

    while queue:
        burned_next = False
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbour in (node.left, node.right, parent.get(node)):
                if neighbour and neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    burned_next = True

        if burned_next:
            time += 1

    return time
