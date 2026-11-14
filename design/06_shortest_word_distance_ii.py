"""LeetCode 244. Shortest Word Distance II (Medium) - Design (index lists + two pointers)
https://leetcode.com/problems/shortest-word-distance-ii/

WordDistance is built once from words_dict, then shortest(word1, word2) is
called many times. Each call returns the smallest index distance between
word1 and word2 in words_dict. Make repeated calls fast.

Constraints: 1 <= len(words_dict) <= 3 * 10^4, word1 != word2, both are in
words_dict, at most 5000 calls to shortest.
"""

from testkit import run


class WordDistance:

    def __init__(self, words_dict: list[str]):
        # TODO: your code here
        pass

    def shortest(self, word1: str, word2: str) -> int:
        raise NotImplementedError


def run_ops(words_dict: list[str], queries: list[tuple[str, str]]) -> list[int]:
    wd = WordDistance(words_dict)
    return [wd.shortest(a, b) for a, b in queries]


if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    run(run_ops, [
        ((words, [("coding", "practice"), ("makes", "coding")]), [3, 1], "official example"),
        ((words, [("practice", "makes"), ("makes", "perfect"), ("perfect", "practice")]),
         [1, 1, 2], "word order in the query doesn't matter"),
        ((["a", "b", "a", "a", "c", "b"], [("a", "c"), ("b", "c"), ("a", "b")]),
         [1, 1, 1], "the closest pair isn't the first copy of each"),
        ((["x", "q", "q", "q", "q", "y"], [("x", "y")]), [5], "far apart"),
    ])
