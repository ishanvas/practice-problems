"""LeetCode 528. Random Pick with Weight (Medium) - Prefix sums + binary search
https://leetcode.com/problems/random-pick-with-weight/

Solution(w) gets positive weights. pickIndex() returns a random index i with
probability w[i] / sum(w).

Constraints: 1 <= len(w) <= 10^4, 1 <= w[i] <= 10^5, at most 10^4 calls to
pickIndex.

Testing note: random picks can't be compared directly, so solve() calls
pickIndex many times and returns each index's share of the picks, rounded to
1 decimal.
"""

from collections import Counter

from testkit import run


class Solution:

    def __init__(self, w: list[int]):
        # TODO: your code here
        pass

    def pickIndex(self) -> int:
        raise NotImplementedError


DRAWS = 20000


def solve(w: list[int]):
    s = Solution(w)
    counts = Counter(s.pickIndex() for _ in range(DRAWS))
    bad = [i for i in counts if not 0 <= i < len(w)]
    if bad:
        return f"index out of range: {bad[:3]}"
    return [round(counts[i] / DRAWS, 1) for i in range(len(w))]


if __name__ == "__main__":
    run(solve, [
        (([1],), [1.0], "official example 1: only one index"),
        (([1, 4],), [0.2, 0.8], "official-style example 2"),
        (([1, 2, 3, 4],), [0.1, 0.2, 0.3, 0.4], "increasing weights"),
        (([3, 1, 1, 5],), [0.3, 0.1, 0.1, 0.5], "unsorted weights"),
        (([100000, 1],), [1.0, 0.0], "huge weight next to a tiny one"),
    ])
