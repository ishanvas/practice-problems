"""LeetCode 215. Kth Largest Element in an Array (Medium) - Heap / Quickselect
https://leetcode.com/problems/kth-largest-element-in-an-array/

Return the kth largest element in nums: the kth largest in sorted order,
not the kth distinct value. Can you do it without sorting?

Constraints: 1 <= k <= len(nums) <= 10^5, -10^4 <= nums[i] <= 10^4.
"""

from testkit import run


def find_kth_largest(nums: list[int], k: int) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(find_kth_largest, [
        (([3, 2, 1, 5, 6, 4], 2), 5, "official example 1"),
        (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4, "official example 2"),
        (([1], 1), 1, "one element"),
        (([2, 2, 2], 2), 2, "duplicates count separately"),
        (([-1, -5, 3], 3), -5, "k = n gives the minimum"),
        (([7, 1, 9, 3], 1), 9, "k = 1 gives the maximum"),
    ])
