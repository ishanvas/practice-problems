"""LeetCode 863. All Nodes Distance K in Binary Tree (Medium) - Tree to graph + BFS
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Given the root of a binary tree, a target node and an integer k, return the
values of all nodes exactly k edges from target, in any order.

Constraints: 1 <= n <= 500, all values are unique, target is in the tree,
0 <= k <= 1000.
"""

from __future__ import annotations

from testkit import run


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_target(node: TreeNode, target: TreeNode, k: int) -> list[list[int]]:
    if not node:
        return []
    
    if node.val == target.val:
        print(f'target found {node.val} {k}')
        return [[node, k, 2]]

    found = []
    if node.left:
        found = find_target(node.left, target, k)
        
        distance_frm_node = k - len(found)
        if found :
            print(f'appending {node.val} {k - len(found)}')
            found.append([node, k - len(found), 1])
            return found

    if node.right:
        found = find_target(node.right, target, k)
        print(f'appending {node.val} {k - len(found)}')
        distance_frm_node = k - len(found)
        if found:
            print(f'appending {node.val} {k - len(found)}')
            found.append([node, k - len(found), 0])
            return found


    return found

def node_at_depth(node: Node, depth:int, side: int) -> list[TreeNode]:
    if not node or depth < 0: 
        return []
    if depth == 0:
        return [node.val]

    nodes = []
    if side == 0 or side == 2:
        found = node_at_depth(node.left, depth - 1, 2)
        nodes = nodes + found
    if side == 1 or side == 2:
        found = node_at_depth(node.left, depth - 1, 2)
        nodes = nodes + found

    return nodes


def distance_k(root: TreeNode, target: TreeNode, k: int) -> list[int]:

    nodes = find_target(root, target, k)
    print(nodes)
    all_nodes = []
    for node, dist, direc in nodes:
        found = node_at_depth(node, dist, direc)
        all_nodes = all_nodes + found
    return all_nodes


# ---- Fixed version: same idea as above, only the bugs changed ----

def find_target_fixed(node: TreeNode, target: TreeNode, k: int) -> list[list]:
    if not node:
        return []

    if node is target:
        return [[node, k, 2]]

    found = find_target_fixed(node.left, target, k)
    if found:                                     # no distance check: keep the path
        found.append([node, k - len(found), 1])   # target on left -> search right
        return found

    found = find_target_fixed(node.right, target, k)
    if found:
        found.append([node, k - len(found), 0])   # target on right -> search left (was 1)
        return found

    return []


def node_at_depth_fixed(node: TreeNode, depth: int, side: int) -> list[int]:
    if not node or depth < 0:
        return []
    if depth == 0:
        return [node.val]

    nodes = []
    if side == 0 or side == 2:
        nodes += node_at_depth_fixed(node.left, depth - 1, 2)    # was 1
    if side == 1 or side == 2:
        nodes += node_at_depth_fixed(node.right, depth - 1, 2)   # was node.left, 1

    return nodes


def distance_k_fixed(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    all_nodes = []
    for node, dist, direc in find_target_fixed(root, target, k):
        all_nodes += node_at_depth_fixed(node, dist, direc)
    return all_nodes


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


def solve(values: list, target_val: int, k: int, fn=distance_k) -> list[int]:
    """Build the tree, find the node holding target_val, and call fn (distance_k by default)."""
    root = build(values)
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == target_val:
            return fn(root, node, k)
        stack += [c for c in (node.left, node.right) if c]
    raise ValueError("target not in tree")


def solve_fixed(values: list, target_val: int, k: int) -> list[int]:
    return solve(values, target_val, k, fn=distance_k_fixed)


if __name__ == "__main__":
    tree = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    run(solve, [
            ((tree, 5, 2), [1, 4, 7], "official example 1"),
        ], check=lambda got, want, args: sorted(got) == want)
    print()
    run(solve_fixed, [
        ((tree, 5, 2), [1, 4, 7], "official example 1"),
        (([1], 1, 3), [], "official example 2: nothing that far"),
        ((tree, 5, 0), [5], "k = 0 is the target itself"),
        ((tree, 3, 1), [1, 5], "target is the root"),
        ((tree, 7, 3), [3, 6], "go up through the parents"),
        ((tree, 7, 1), [2], "ancestors past k must not lose the path"),
        ((tree, 6, 3), [1, 4, 7], "mix of up-then-down paths"),
        ((tree, 6, 4), [0, 8], "up to the root and down the other side"),
    ], check=lambda got, want, args: sorted(got) == want)
    """
    run(solve, [
        ((tree, 5, 2), [1, 4, 7], "official example 1"),
        (([1], 1, 3), [], "official example 2: nothing that far"),
        ((tree, 5, 0), [5], "k = 0 is the target itself"),
        ((tree, 3, 1), [1, 5], "target is the root"),
        ((tree, 7, 3), [3, 6], "go up through the parents"),
        ((tree, 6, 3), [1, 4, 7], "mix of up-then-down paths"),
        ((tree, 6, 4), [0, 8], "up to the root and down the other side"),
    ], check=lambda got, want, args: sorted(got) == want)
    """
