"""LeetCode 152. Maximum Product Subarray (Medium) - DP (track max and min)
https://leetcode.com/problems/maximum-product-subarray/

Return the largest product of a non-empty contiguous subarray of nums.

Hint: a negative number turns the smallest product into the largest, so
track both the max and the min ending at each index.

Constraints: 1 <= len(nums) <= 2 * 10^4, -10 <= nums[i] <= 10.
"""

from testkit import run


def max_product(nums: list[int]) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(max_product, [
        (([2, 3, -2, 4],), 6, "official example 1"),
        (([-2, 0, -1],), 0, "official example 2"),
        (([-2, 3, -4],), 24, "two negatives cancel"),
        (([-2],), -2, "one negative number"),
        (([0, 2],), 2, "zero resets"),
        (([-1, -2, -3],), 6, "best is a prefix"),
        (([2, -5, -2, -4, 3],), 24, "best is -2 * -4 * 3"),
    ])
