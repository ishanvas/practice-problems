"""LeetCode 752. Open the Lock (Medium) - BFS
https://leetcode.com/problems/open-the-lock/

A lock has 4 wheels, each showing 0-9, and starts at "0000". One move turns
one wheel by one slot, and the digits wrap around (9 -> 0 and 0 -> 9). The
lock jams if it ever shows a code in deadends. Return the fewest moves to
reach target, or -1 if it can't be reached.

Constraints: 1 <= len(deadends) <= 500 on LeetCode (empty lists are also
tested here), every code is 4 digits, and target is not in deadends.
"""

from testkit import run


def open_lock(deadends: list[str], target: str) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    around_8888 = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    run(open_lock, [
        ((["0201", "0101", "0102", "1212", "2002"], "0202"), 6, "official example 1"),
        ((["8888"], "0009"), 1, "official example 2: 0 -> 9 wraps"),
        ((around_8888, "8888"), -1, "official example 3: every neighbour of the target is dead"),
        ((["0000"], "8888"), -1, "the start itself is dead"),
        (([], "0000"), 0, "already open"),
        (([], "9999"), 4, "wrap every wheel backwards"),
        (([], "5555"), 20, "5 turns per wheel, either way round"),
    ])
