"""LeetCode 277. Find the Celebrity (Medium) - Graph / elimination
https://leetcode.com/problems/find-the-celebrity/

There are n people at a party, labelled 0 to n - 1. A celebrity is known by
everyone else and knows nobody else. You can only ask knows(a, b): "does a
know b?" Return the celebrity's label, or -1 if there isn't one. There is at
most one celebrity.

LeetCode gives you knows() as a global function. Here it's passed in.

Follow-up: use at most 3 * n calls to knows. The tests enforce this.

Constraints: 2 <= n <= 100 on LeetCode (n = 1 is also tested here).
"""

from typing import Callable

from testkit import run


def find_celebrity(n: int, knows: Callable[[int, int], bool]) -> int:
    # TODO: your code here
    raise NotImplementedError


def solve(graph: list[list[int]]) -> int:
    """graph[a][b] == 1 means a knows b. Fails if knows() is called over 3n times."""
    n, calls = len(graph), 0

    def knows(a, b):
        nonlocal calls
        calls += 1
        if calls > 3 * n:
            raise RuntimeError(f"more than 3n = {3 * n} calls to knows()")
        return graph[a][b] == 1

    return find_celebrity(n, knows)


if __name__ == "__main__":
    run(solve, [
        (([[1, 1, 0], [0, 1, 0], [1, 1, 1]],), 1, "official example 1"),
        (([[1, 0, 1], [1, 1, 0], [0, 1, 1]],), -1, "official example 2"),
        (([[1, 0], [1, 1]],), 0, "two people"),
        (([[1, 1], [1, 1]],), -1, "they know each other"),
        (([[1]],), 0, "one person"),
        (([[1, 0, 0], [0, 1, 0], [1, 0, 1]],), -1, "0 knows nobody, but 1 doesn't know 0"),
        (([[1, 1, 1, 1], [0, 1, 0, 1], [0, 1, 1, 1], [0, 0, 0, 1]],), 3, "celebrity is last"),
    ])
