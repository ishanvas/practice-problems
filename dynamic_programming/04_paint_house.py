"""LeetCode 256. Paint House (Medium) - DP
https://leetcode.com/problems/paint-house/

costs[i] = [red, blue, green] is the cost to paint house i each colour. No
two neighbouring houses may be the same colour. Return the minimum total
cost to paint every house.

Constraints: 1 <= len(costs) <= 100, 1 <= costs[i][j] <= 20.
"""

from testkit import run


def min_cost(costs: list[list[int]]) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(min_cost, [
        (([[17, 2, 17], [16, 16, 5], [14, 3, 19]],), 10, "official example 1: blue, green, blue"),
        (([[7, 6, 2]],), 2, "official example 2"),
        (([[1, 2, 3], [1, 2, 3]],), 3, "the cheapest colour can't be used twice in a row"),
        (([[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 15, 17], [3, 20, 10]],), 43,
         "greedy per house isn't optimal"),
        (([[1, 20, 20], [20, 1, 20], [20, 20, 1], [1, 20, 20]],), 4, "cheapest colour changes every house"),
    ])
