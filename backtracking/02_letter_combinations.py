"""LeetCode 17. Letter Combinations of a Phone Number (Medium) - Backtracking
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Each digit 2-9 maps to letters as on a phone keypad:
2 abc, 3 def, 4 ghi, 5 jkl, 6 mno, 7 pqrs, 8 tuv, 9 wxyz.
Return every letter string that digits could spell, in any order.

Constraints: 0 <= len(digits) <= 4, digits are 2-9.
"""

from testkit import run


def letter_combinations(digits: str) -> list[str]:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(letter_combinations, [
        (("23",), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "official example 1"),
        (("",), [], "official example 2: empty input gives [], not ['']"),
        (("2",), ["a", "b", "c"], "official example 3"),
        (("7",), ["p", "q", "r", "s"], "a 4-letter key"),
        (("79",), ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz",
                   "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"], "two 4-letter keys"),
        (("22",), ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"], "same digit twice"),
    ], check=lambda got, want, args: sorted(got) == want)
