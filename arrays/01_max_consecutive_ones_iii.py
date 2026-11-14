"""LeetCode 1004. Max Consecutive Ones III (Medium) - Sliding window
https://leetcode.com/problems/max-consecutive-ones-iii/

nums is a binary array. You may flip at most k zeros to ones. Return the
length of the longest run of consecutive ones you can get.

Hint: find the longest window that holds at most k zeros.

Constraints: 1 <= len(nums) <= 10^5, 0 <= k <= len(nums).
"""

from testkit import run


def longest_ones(nums: list[int], k: int) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(longest_ones, [
        (([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6, "official example 1"),
        (([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10, "official example 2"),
        (([0, 0, 0], 0), 0, "no flips, no ones"),
        (([1, 1, 1], 0), 3, "already all ones"),
        (([0, 0, 0], 5), 3, "k bigger than the number of zeros"),
        (([1, 0, 1, 0, 1], 1), 3, "one flip, two equal choices"),
    ])
