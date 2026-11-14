"""LeetCode 787. Cheapest Flights Within K Stops (Medium) - Bellman-Ford
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities labelled 0 to n - 1. flights[i] = [from, to, price] is a
one-way flight. Return the cheapest price from src to dst using at most k
stops (cities in between), or -1 if there's no such route.

Constraints: 1 <= n <= 100, src != dst, 0 <= k < n.
"""

from testkit import run


def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    triangle = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    run(find_cheapest_price, [
        ((4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1),
         700, "official example 1: 0->1->2->3 is cheaper but has 2 stops"),
        ((3, triangle, 0, 2, 1), 200, "official example 2"),
        ((3, triangle, 0, 2, 0), 500, "official example 3: no stops allowed"),
        ((3, [[0, 1, 100]], 0, 2, 1), -1, "dst unreachable"),
        ((4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1),
         6, "cheapest way to 2 goes via 1, but then 3 needs too many stops"),
    ])
