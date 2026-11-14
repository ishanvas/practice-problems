"""LeetCode 61. Rotate List (Medium) - Linked list
https://leetcode.com/problems/rotate-list/

Rotate a linked list to the right by k places and return the new head.
Example: 1->2->3->4->5 with k = 2 becomes 4->5->1->2->3.

Hint: k can be far bigger than the list's length.

Constraints: 0 <= n <= 500, 0 <= k <= 2 * 10^9.
"""

from __future__ import annotations

from testkit import run


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    # TODO: your code here
    raise NotImplementedError


def build(values: list[int]) -> ListNode | None:
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head: ListNode | None, limit: int = 1000) -> list:
    out = []
    while head and len(out) < limit:
        out.append(head.val)
        head = head.next
    if head:
        out.append("... (cycle?)")
    return out


def solve(values: list[int], k: int) -> list:
    return to_list(rotate_right(build(values), k))


if __name__ == "__main__":
    run(solve, [
        (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3], "official example 1"),
        (([0, 1, 2], 4), [2, 0, 1], "official example 2: k > length"),
        (([], 0), [], "empty list"),
        (([], 5), [], "empty list, k > 0 (don't divide by zero)"),
        (([1], 99), [1], "one node"),
        (([1, 2], 2), [1, 2], "k = length is a full turn"),
        (([1, 2, 3], 2_000_000_000), [2, 3, 1], "huge k: use k % length"),
    ])
