"""LeetCode 200. Number of Islands (Medium) - DFS / BFS flood fill
https://leetcode.com/problems/number-of-islands/

grid is an m x n map of "1" (land) and "0" (water). Return the number of
islands. An island is land connected up, down, left or right (not
diagonally). Everything outside the grid is water.

Constraints: 1 <= m, n <= 300.
"""

from testkit import run


def num_islands(grid: list[list[str]]) -> int:
    # TODO: your code here
    raise NotImplementedError


def g(*rows: str) -> list[list[str]]:
    """g("110", "011") -> [["1","1","0"], ["0","1","1"]]"""
    return [list(r) for r in rows]


if __name__ == "__main__":
    run(num_islands, [
        ((g("11110", "11010", "11000", "00000"),), 1, "official example 1"),
        ((g("11000", "11000", "00100", "00011"),), 3, "official example 2"),
        ((g("000", "000"),), 0, "all water"),
        ((g("1"),), 1, "one cell"),
        ((g("10", "01"),), 2, "diagonal doesn't connect"),
        ((g("111", "001", "111"),), 1, "snake shape"),
        ((g("101", "010", "101"),), 5, "checkerboard"),
    ])
