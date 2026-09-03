"""
Children Sum Property in Binary Tree

Pattern:
Recursive tree mutation

Key idea:
Push larger parent values down, then fix parents on the way back.

Time: O(N)
Space: O(H)
"""

from __future__ import annotations

from typing import Optional


def is_children_sum(root: Optional["TreeNode"]) -> bool:
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True

    child_sum = 0
    if root.left:
        child_sum += root.left.val
    if root.right:
        child_sum += root.right.val

    return (
        root.val == child_sum
        and is_children_sum(root.left)
        and is_children_sum(root.right)
    )


def change_to_children_sum(root: Optional["TreeNode"]) -> None:
    if root is None:
        return

    child_sum = 0
    if root.left:
        child_sum += root.left.val
    if root.right:
        child_sum += root.right.val

    if child_sum >= root.val:
        root.val = child_sum
    else:
        if root.left:
            root.left.val = root.val
        if root.right:
            root.right.val = root.val

    change_to_children_sum(root.left)
    change_to_children_sum(root.right)

    total = 0
    if root.left:
        total += root.left.val
    if root.right:
        total += root.right.val
    if root.left or root.right:
        root.val = total
