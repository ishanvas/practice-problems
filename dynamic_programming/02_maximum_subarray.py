"""LeetCode 53. Maximum Subarray (Medium) - Kadane's algorithm
https://leetcode.com/problems/maximum-subarray/

Return the largest sum of a non-empty contiguous subarray of nums.

Follow-up: once O(n) works, try divide and conquer.

Constraints: 1 <= len(nums) <= 10^5, -10^4 <= nums[i] <= 10^4.
"""

from testkit import run


def max_sub_array(nums: list[int]) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(max_sub_array, [
        (([-2, 1, -3, 4, -1, 2, 1, -5, 4],), 6, "official example 1: [4,-1,2,1]"),
        (([1],), 1, "official example 2"),
        (([5, 4, -1, 7, 8],), 23, "official example 3: the whole array"),
        (([-3, -1, -2],), -1, "all negative: subarray can't be empty"),
        (([-1],), -1, "one negative number"),
        (([2, -5, 3],), 3, "restart after a drop"),
    ])
