"""LeetCode 339. Nested List Weight Sum (Medium) - DFS / BFS
https://leetcode.com/problems/nested-list-weight-sum/

nested_list holds integers and lists, which can hold more integers and
lists. An integer's depth is how many lists it's inside, so top-level
integers have depth 1. Return the sum of every integer times its depth.

Example: [1, [4, [6]]] -> 1*1 + 4*2 + 6*3 = 27.

You only get the NestedInteger interface below, as on LeetCode.

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


def depth_sum(nested_list: list[NestedInteger]) -> int:
    # TODO: your code here
    raise NotImplementedError


def solve(raw: list) -> int:
    return depth_sum([NestedInteger(x) for x in raw])


if __name__ == "__main__":
    run(solve, [
        (([[1, 1], 2, [1, 1]],), 10, "official example 1"),
        (([1, [4, [6]]],), 27, "official example 2"),
        (([0],), 0, "official example 3"),
        (([[], 3],), 3, "empty inner list"),
        (([-1, [2]],), 3, "negative values"),
        (([[[[5]]]],), 20, "deep nesting: 5 at depth 4"),
    ])
