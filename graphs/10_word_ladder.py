"""LeetCode 127. Word Ladder (Hard) - BFS
https://leetcode.com/problems/word-ladder/

A transformation sequence goes from begin_word to end_word, changing one
letter at a time. Every word after begin_word must be in word_list
(begin_word doesn't have to be). Return the number of words in the shortest
sequence, or 0 if there's none.

Constraints: 1 <= len(begin_word) <= 10, all words have the same length,
lowercase letters only, 1 <= len(word_list) <= 5000, begin_word != end_word.
"""

from testkit import run


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(ladder_length, [
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5, "official example 1"),
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0, "official example 2: end_word not in list"),
        (("a", "c", ["a", "b", "c"]), 2, "one-letter words"),
        (("hot", "dot", ["dot"]), 2, "one step"),
        (("hot", "dog", ["hot", "dog"]), 0, "two letters apart, nothing in between"),
        (("lost", "miss", ["most", "mist", "miss", "lost", "fist", "fish"]), 4, "lost->most->mist->miss"),
    ])
