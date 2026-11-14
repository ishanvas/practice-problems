"""LeetCode 617. Merge Two Binary Trees (Easy) - DFS
https://leetcode.com/problems/merge-two-binary-trees/

Lay root2 over root1. Where both trees have a node, the merged node's value
is the sum. Where only one tree has a node, use that node. Return the merged
tree.

Constraints: 0 <= n <= 2000 in each tree.
"""

from __future__ import annotations

from testkit import run


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
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


def to_list(root: TreeNode | None) -> list:
    """Turn a tree back into a LeetCode-style level-order list."""
    out, queue = [], [root]
    for node in queue:
        out.append(node.val if node else None)
        if node:
            queue += [node.left, node.right]
    while out and out[-1] is None:
        out.pop()
    return out


def solve(values1: list, values2: list) -> list:
    return to_list(merge_trees(build(values1), build(values2)))


if __name__ == "__main__":
    run(solve, [
        (([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7]), [3, 4, 5, 5, 4, None, 7], "official example 1"),
        (([1], [1, 2]), [2, 2], "official example 2"),
        (([], []), [], "both empty"),
        (([], [1, 2]), [1, 2], "first tree empty"),
        (([1, 2], []), [1, 2], "second tree empty"),
        (([1, None, 2, None, 3], [1, 2]), [2, 2, 2, None, None, None, 3], "trees grow in opposite directions"),
    ])
