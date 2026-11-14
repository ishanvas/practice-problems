"""LeetCode 364. Nested List Weight Sum II (Medium) - BFS by level
https://leetcode.com/problems/nested-list-weight-sum-ii/

Same input as 01_nested_list_weight_sum.py, but the weights are reversed.
An integer's weight is max_depth - depth + 1, so the deepest integers count
once and top-level integers count the most. max_depth is the deepest depth
of any integer.

Example: [1, [4, [6]]] -> max_depth 3 -> 1*3 + 4*2 + 6*1 = 17.

Hint: you can do it in one BFS pass without knowing max_depth in advance.

Constraints: 1 <= len(nested_list) <= 50, -100 <= values <= 100,
max depth <= 50.
"""

from __future__ import annotations

from testkit import run


class NestedInteger:
    """LeetCode's interface. Use isInteger(), getInteger() and getList()."""

    def __init__(self, value):
        self._value = value if isinstance(value, int) else [NestedInteger(v) for v in value]

    def isInteger(self) -> bool:
        return isinstance(self._value, int)

    def getInteger(self) -> int | None:
        return self._value if self.isInteger() else None

    def getList(self) -> list["NestedInteger"] | None:
        return None if self.isInteger() else self._value


def depth_sum_inverse(nested_list: list[NestedInteger]) -> int:
    # TODO: your code here
    raise NotImplementedError


def solve(raw: list) -> int:
    return depth_sum_inverse([NestedInteger(x) for x in raw])


if __name__ == "__main__":
    run(solve, [
        (([[1, 1], 2, [1, 1]],), 8, "official example 1"),
        (([1, [4, [6]]],), 17, "official example 2"),
        (([5],), 5, "one integer"),
        (([[1], [[2]], 3],), 13, "1*2 + 2*1 + 3*3"),
        (([[[-1]], 2],), 5, "negative value at the deepest level"),
    ])
