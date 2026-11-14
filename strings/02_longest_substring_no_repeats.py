"""LeetCode 3. Longest Substring Without Repeating Characters (Medium) - Sliding window
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Return the length of the longest substring of s (contiguous, not a
subsequence) with no repeated characters.

Constraints: 0 <= len(s) <= 5 * 10^4. s can have letters, digits, symbols
and spaces.
"""

from testkit import run


def length_of_longest_substring(s: str) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(length_of_longest_substring, [
        (("abcabcbb",), 3, "official example 1: abc"),
        (("bbbbb",), 1, "official example 2"),
        (("pwwkew",), 3, "official example 3: wke, not the subsequence pwke"),
        (("",), 0, "empty string"),
        ((" ",), 1, "a space counts as a character"),
        (("dvdf",), 3, "vdf: the window shrinks only past the first d"),
        (("abba",), 2, "the left edge must never move backwards"),
        (("tmmzuxt",), 5, "mzuxt"),
    ])
