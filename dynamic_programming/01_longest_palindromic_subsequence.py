"""LeetCode 516. Longest Palindromic Subsequence (Medium) - Interval DP
https://leetcode.com/problems/longest-palindromic-subsequence/

Return the length of the longest palindromic subsequence in s. A subsequence
keeps the original order but may skip characters.

Hint: dp[i][j] = answer for s[i..j]. If s[i] == s[j], use both ends.
Otherwise drop one end.

Constraints: 1 <= len(s) <= 1000, lowercase letters only.
"""

from testkit import run


def longest_palindrome_subseq(s: str) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(longest_palindrome_subseq, [
        (("bbbab",), 4, "official example 1: bbbb"),
        (("cbbd",), 2, "official example 2: bb"),
        (("a",), 1, "one character"),
        (("abcde",), 1, "all different"),
        (("aaaa",), 4, "whole string"),
        (("agbdba",), 5, "abdba, skipping g"),
        (("character",), 5, "carac"),
    ])
