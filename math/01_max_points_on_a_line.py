"""LeetCode 149. Max Points on a Line (Hard) - Math / slope hashing
https://leetcode.com/problems/max-points-on-a-line/

points[i] = [x, y] is a point on a plane. Return the largest number of
points that lie on one straight line.

Hint: float slopes can compare as equal when they aren't. Store each slope as
a reduced fraction (dy, dx) instead.

Constraints: 1 <= len(points) <= 300, -10^4 <= x, y <= 10^4, all points are
unique.
"""

from testkit import run


def max_points(points: list[list[int]]) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(max_points, [
        (([[1, 1], [2, 2], [3, 3]],), 3, "official example 1"),
        (([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],), 4, "official example 2"),
        (([[0, 0]],), 1, "one point"),
        (([[0, 0], [5, 7]],), 2, "two points always share a line"),
        (([[1, 1], [1, 2], [1, 5], [2, 3]],), 3, "vertical line (dx = 0)"),
        (([[0, 3], [5, 3], [-2, 3], [1, 1]],), 3, "horizontal line (dy = 0)"),
        (([[0, 0], [1, -1], [-1, 1], [2, 1]],), 3, "(1,-1) and (-1,1) are the same slope"),
        (([[0, 0], [94911151, 94911150], [94911152, 94911151]],), 2, "float slopes look equal but aren't"),
    ])
