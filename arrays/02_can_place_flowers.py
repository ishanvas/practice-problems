"""LeetCode 605. Can Place Flowers (Easy) - Greedy
https://leetcode.com/problems/can-place-flowers/

flowerbed is a list of 0s (empty) and 1s (planted). Flowers can't be planted
in adjacent plots. Return whether n new flowers can be planted without
breaking that rule.

Constraints: 1 <= len(flowerbed) <= 2 * 10^4, the input has no adjacent 1s,
0 <= n <= len(flowerbed).
"""

from testkit import run


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(can_place_flowers, [
        (([1, 0, 0, 0, 1], 1), True, "official example 1"),
        (([1, 0, 0, 0, 1], 2), False, "official example 2"),
        (([0], 1), True, "one empty plot"),
        (([0, 0, 1, 0, 0], 2), True, "both ends are usable"),
        (([1, 0, 1], 1), False, "the gap is too small"),
        (([0, 0, 0], 2), True, "plant at both ends"),
        (([1], 0), True, "n = 0 always works"),
        (([0, 0, 0, 0], 3), False, "greedy fits only 2"),
    ])
