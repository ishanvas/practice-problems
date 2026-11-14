"""LeetCode 272. Closest Binary Search Tree Value II (Hard) - BST inorder / two stacks
https://leetcode.com/problems/closest-binary-search-tree-value-ii/

Given the root of a binary search tree, a float target and an integer k,
return the k values in the tree closest to target, in any order. There is
exactly one correct set of k values.

Follow-up: if the BST is balanced, can you beat O(n)?

Constraints: 1 <= k <= n <= 10^4, 0 <= Node.val <= 10^9.
"""

from __future__ import annotations

from testkit import run


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_k_values(root: TreeNode | None, target: float, k: int) -> list[int]:
    # TODO: your code here
    raise NotImplementedError


def build(values: list) -> TreeNode | None:
    """Build a tree from a LeetCode-style level-order list, None for gaps."""
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = iter(nodes[1:])
    for node in nodes:
        if node:
            node.left = next(kids, None)
            node.right = next(kids, None)
    return nodes[0]


def solve(values: list, target: float, k: int) -> list[int]:
    return closest_k_values(build(values), target, k)


if __name__ == "__main__":
    tree = [8, 4, 12, 2, 6, 10, 14]
    run(solve, [
        (([4, 2, 5, 1, 3], 3.714286, 2), [3, 4], "official example 1"),
        (([1], 0.0, 1), [1], "official example 2"),
        (([4, 2, 5, 1, 3], 0.0, 3), [1, 2, 3], "target below every value"),
        (([4, 2, 5, 1, 3], 10.0, 2), [4, 5], "target above every value"),
        (([2, 1, 3], 2.0, 3), [1, 2, 3], "k = n"),
        ((tree, 7.2, 3), [6, 8, 10], "answer spans both sides of the target"),
        (([5, 3, None, 1, None, None, 2], 2.2, 2), [2, 3], "skewed tree"),
    ], check=lambda got, want, args: sorted(got) == want)
