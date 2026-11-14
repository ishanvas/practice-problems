"""LeetCode 366. Find Leaves of Binary Tree (Medium) - DFS by height
https://leetcode.com/problems/find-leaves-of-binary-tree/

Repeatedly collect all the leaves of the tree and remove them, until the
tree is empty. Return the groups in the order they were removed. The order
inside a group doesn't matter.

Hint: a node is removed in round = its height (leaves have height 0).

Constraints: 1 <= n <= 100.
"""

from __future__ import annotations

from testkit import run


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_leaves(root: TreeNode | None) -> list[list[int]]:
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


def solve(values: list) -> list[list[int]]:
    return find_leaves(build(values))


if __name__ == "__main__":
    run(solve, [
        (([1, 2, 3, 4, 5],), [[3, 4, 5], [2], [1]], "official example 1"),
        (([1],), [[1]], "official example 2"),
        (([1, 2, None, 3],), [[3], [2], [1]], "a chain"),
        (([1, 2, 3, 4, None, None, None, 5],), [[3, 5], [4], [2], [1]],
         "grouped by height, not depth: 3 is shallow but goes first"),
    ], check=lambda got, want, args: [sorted(g) for g in got] == want)
