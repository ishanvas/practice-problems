"""LeetCode 360. Sort Transformed Array (Medium) - Math + two pointers
https://leetcode.com/problems/sort-transformed-array/

nums is sorted ascending. Apply f(x) = a*x^2 + b*x + c to every element and
return the results sorted ascending. Can you do it in O(n)?

Hint: when a > 0 the biggest values are at the two ends of nums, and when
a < 0 the smallest are.

Constraints: 1 <= len(nums) <= 200, -100 <= nums[i], a, b, c <= 100.
"""

from testkit import run


def sort_transformed_array(nums: list[int], a: int, b: int, c: int) -> list[int]:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    nums = [-4, -2, 2, 4]
    run(sort_transformed_array, [
        ((nums, 1, 3, 5), [3, 9, 15, 33], "official example 1: opens upward"),
        ((nums, -1, 3, 5), [-23, -5, 1, 7], "official example 2: opens downward"),
        ((nums, 0, 2, 1), [-7, -3, 5, 9], "a = 0, rising line"),
        ((nums, 0, -2, 1), [-7, -3, 5, 9], "a = 0, falling line"),
        (([5], 2, 0, 0), [50], "one element"),
        (([-3, -1, 0, 2], 0, 0, 7), [7, 7, 7, 7], "constant function"),
        (([-1, 0, 1, 2, 3], 1, -2, 0), [-1, 0, 0, 3, 3], "vertex inside the range, with ties"),
    ])
