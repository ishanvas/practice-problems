"""LeetCode 104. Maximum Depth of Binary Tree (Easy) - DFS / BFS
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Return the number of nodes on the longest path from the root down to a leaf.

Constraints: 0 <= n <= 10^4.
"""

from __future__ import annotations

from testkit import run


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
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


def solve(values: list) -> int:
    return max_depth(build(values))


if __name__ == "__main__":
    run(solve, [
        (([3, 9, 20, None, None, 15, 7],), 3, "official example 1"),
        (([1, None, 2],), 2, "official example 2"),
        (([],), 0, "empty tree"),
        (([1],), 1, "just the root"),
        (([1, 2, 3, 4, None, None, None, 5],), 4, "deepest leaf is on the left"),
        ((list(range(1, 16)),), 4, "perfect tree with 15 nodes"),
    ])
