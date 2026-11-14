"""LeetCode 1334. Find the City With the Smallest Number of Neighbors at a
Threshold Distance (Medium) - Floyd-Warshall
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

There are n cities labelled 0 to n - 1. edges[i] = [a, b, w] is a two-way road
of length w. For each city, count how many other cities it can reach with a
shortest path of at most distance_threshold. Return the city with the smallest
count. If there's a tie, return the one with the largest label.

Constraints: 2 <= n <= 100, 1 <= w, distance_threshold <= 10^4.
"""

from testkit import run


def find_the_city(n: int, edges: list[list[int]], distance_threshold: int) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(find_the_city, [
        ((4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4), 3, "official example 1"),
        ((5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2), 0, "official example 2"),
        ((2, [[0, 1, 1]], 1), 1, "tie: pick the larger label"),
        ((3, [], 5), 2, "no roads: everyone has 0 neighbours"),
        ((3, [[0, 1, 1], [1, 2, 1]], 1), 2, "0 and 2 are 2 apart, over the threshold"),
        ((3, [[0, 1, 1], [1, 2, 1], [0, 2, 10]], 2), 2, "road 0-2 is long, but the path via 1 is short"),
    ])
