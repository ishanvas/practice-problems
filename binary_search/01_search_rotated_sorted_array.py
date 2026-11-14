"""LeetCode 33. Search in Rotated Sorted Array (Medium) - Binary search
https://leetcode.com/problems/search-in-rotated-sorted-array/

nums was sorted ascending with distinct values, then possibly rotated at an
unknown index (e.g. [0,1,2,4,5,6,7] -> [4,5,6,7,0,1,2]). Return the index of
target, or -1 if it's not there. Your solution must run in O(log n).

Constraints: 1 <= len(nums) <= 5000, all values are distinct.
"""

from testkit import run


def search(nums: list[int], target: int) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    rotated = [4, 5, 6, 7, 0, 1, 2]
    run(search, [
        ((rotated, 0), 4, "official example 1"),
        ((rotated, 3), -1, "official example 2"),
        (([1], 0), -1, "official example 3"),
        ((rotated, 7), 3, "target is just before the rotation point"),
        (([1, 3, 5, 7], 5), 2, "not rotated at all"),
        (([5, 1, 3], 5), 0, "target is the first element"),
        (([3, 1], 1), 1, "two elements"),
        (([6, 7, 1, 2, 3, 4, 5], 7), 1, "short left half"),
    ])
