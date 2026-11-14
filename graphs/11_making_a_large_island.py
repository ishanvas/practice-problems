"""LeetCode 827. Making A Large Island (Hard) - DFS / island labelling
https://leetcode.com/problems/making-a-large-island/

grid is an n x n binary matrix (1 = land). You may change at most one 0 to 1.
Return the size of the largest island after that change. An island is a
group of 1s connected up, down, left or right.

Constraints: 1 <= n <= 500.
"""

from testkit import run


def largest_island(grid: list[list[int]]) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(largest_island, [
        (([[1, 0], [0, 1]],), 3, "official example 1"),
        (([[1, 1], [1, 0]],), 4, "official example 2"),
        (([[1, 1], [1, 1]],), 4, "official example 3: no 0 to flip"),
        (([[0, 0], [0, 0]],), 1, "all water"),
        (([[1, 0, 1], [0, 0, 0], [1, 0, 1]],), 3, "the centre touches no land, an edge cell joins two"),
        (([[1, 1, 1], [1, 0, 1], [1, 1, 1]],), 9, "same island on all 4 sides: count it once"),
        (([[1, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],), 4, "join islands of size 1 and 2"),
    ])
