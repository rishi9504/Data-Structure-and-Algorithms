"""
LeetCode 863 - All Nodes Distance K in Binary Tree

Pattern:
Parent map + BFS

Key idea:
Treat parent as another neighbour of each node.

Time: O(N)
Space: O(N)
"""

from __future__ import annotations

from collections import deque
from typing import Deque, Dict, List, Optional, Set


class Solution:
    def distanceK(
        self,
        root: Optional["TreeNode"],
        target: "TreeNode",
        k: int,
    ) -> List[int]:
        if root is None:
            return []

        parent: Dict["TreeNode", "TreeNode"] = {}
        queue: Deque["TreeNode"] = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        visited: Set["TreeNode"] = {target}
        queue = deque([target])
        distance = 0

        while queue and distance < k:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbour in (node.left, node.right, parent.get(node)):
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            distance += 1

        return [node.val for node in queue]
