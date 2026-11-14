"""LeetCode 698. Partition to K Equal Sum Subsets (Medium) - Backtracking / bitmask DP
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Return whether nums can be split into k non-empty groups with equal sums.

Hint: each group must sum to sum(nums) / k. Sorting nums in descending order
prunes the search a lot.

Constraints: 1 <= k <= len(nums) <= 16, 1 <= nums[i] <= 10^4.
"""

from testkit import run


def can_partition_k_subsets(nums: list[int], k: int) -> bool:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(can_partition_k_subsets, [
        (([4, 3, 2, 3, 5, 2, 1], 4), True, "official example 1: (5) (1,4) (2,3) (2,3)"),
        (([1, 2, 3, 4], 3), False, "official example 2: sum isn't divisible by 3"),
        (([2, 2, 2, 2, 3, 4, 5], 4), False, "sum divides evenly, but no split works"),
        (([5, 1, 1, 1], 2), False, "one number is bigger than the group sum"),
        (([1, 1, 1, 1], 4), True, "k = n"),
        (([7, 3, 2], 1), True, "k = 1"),
        (([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3), True, "three groups of 10+7+7+6"),
        (([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3], 3), True, "(5,5,3,3) (5,5,3,3) (4,4,4,4)"),
    ])
