"""LeetCode 20. Valid Parentheses (Easy) - Stack
https://leetcode.com/problems/valid-parentheses/

s contains only the characters ()[]{}. Return whether every opening bracket
is closed by the same type of bracket, in the right order.

Constraints: 1 <= len(s) <= 10^4.
"""

from testkit import run


def is_valid(s: str) -> bool:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(is_valid, [
        (("()",), True, "official example 1"),
        (("()[]{}",), True, "official example 2"),
        (("(]",), False, "official example 3"),
        (("([])",), True, "official example 4: nested"),
        (("([)]",), False, "official example 5: crossed"),
        (("(",), False, "never closed"),
        ((")",), False, "closing with nothing open"),
        (("{[]}",), True, "nested mix"),
        (("((",), False, "stack not empty at the end"),
        (("){",), False, "close before open"),
    ])
