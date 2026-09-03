"""
Boundary Traversal of Binary Tree

Pattern:
Boundary walk

Key idea:
Root, left boundary, leaves, then reversed right boundary.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import List, Optional


def boundary_traversal(root: Optional["TreeNode"]) -> List[int]:
    if root is None:
        return []

    def is_leaf(node: "TreeNode") -> bool:
        return node.left is None and node.right is None

    result: List[int] = []
    if not is_leaf(root):
        result.append(root.val)

    def add_left_boundary(node: Optional["TreeNode"]) -> None:
        while node:
            if not is_leaf(node):
                result.append(node.val)
            node = node.left if node.left else node.right

    def add_leaves(node: Optional["TreeNode"]) -> None:
        if node is None:
            return
        if is_leaf(node):
            result.append(node.val)
            return
        add_leaves(node.left)
        add_leaves(node.right)

    def add_right_boundary(node: Optional["TreeNode"]) -> None:
        temp: List[int] = []
        while node:
            if not is_leaf(node):
                temp.append(node.val)
            node = node.right if node.right else node.left
        result.extend(reversed(temp))

    add_left_boundary(root.left)
    add_leaves(root)
    add_right_boundary(root.right)

    return result
