"""LeetCode 886. Possible Bipartition (Medium) - bipartite check
https://leetcode.com/problems/possible-bipartition/

There are n people labelled 1 to n. dislikes[i] = [a, b] means a and b
dislike each other and can't be in the same group. Return True if everyone
can be split into two groups this way, otherwise False.

Constraints: 1 <= n <= 2000, 0 <= len(dislikes) <= 10^4.
"""

from testkit import run


def possible_bipartition(n: int, dislikes: list[list[int]]) -> bool:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(possible_bipartition, [
        ((4, [[1, 2], [1, 3], [2, 4]]), True, "official example 1: groups [1,4] and [2,3]"),
        ((3, [[1, 2], [1, 3], [2, 3]]), False, "official example 2: triangle"),
        ((5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]), False, "odd cycle of 5"),
        ((4, [[1, 2], [2, 3], [3, 4], [4, 1]]), True, "even cycle of 4"),
        ((1, []), True, "one person"),
        ((6, [[1, 2], [2, 3], [4, 5], [5, 6], [4, 6]]), False, "only the second group of people conflicts"),
    ])
