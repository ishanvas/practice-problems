"""LeetCode 744. Find Smallest Letter Greater Than Target (Easy) - Binary search
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

letters is sorted ascending and has at least two different letters. Return
the smallest letter strictly greater than target. If there isn't one, wrap
around and return letters[0].

Constraints: 2 <= len(letters) <= 10^4, lowercase letters only.
"""

from testkit import run


def next_greatest_letter(letters: list[str], target: str) -> str:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    cfj = ["c", "f", "j"]
    run(next_greatest_letter, [
        ((cfj, "a"), "c", "official example 1"),
        ((cfj, "c"), "f", "official example 2: strictly greater"),
        ((["x", "x", "y", "y"], "z"), "x", "official example 3: wraps around"),
        ((cfj, "d"), "f", "target between letters"),
        ((cfj, "j"), "c", "target equals the last letter: wrap"),
        ((["e", "e", "e", "k", "q", "q", "q"], "e"), "k", "skip all copies of target"),
    ])
