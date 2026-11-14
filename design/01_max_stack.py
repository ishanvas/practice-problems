"""LeetCode 716. Max Stack (Hard) - Design (two stacks, or heap + lazy deletion)
https://leetcode.com/problems/max-stack/

Design a stack that also supports finding and removing the largest element.

  push(x)    push x onto the stack
  pop()      remove the top element and return it
  top()      return the top element without removing it
  peekMax()  return the largest element without removing it
  popMax()   remove the largest element and return it. If there are several,
             remove the one closest to the top.

Follow-up: top() in O(1) and every other call in O(log n).

Constraints: -10^7 <= x <= 10^7, at most 10^5 calls, and pop, top, peekMax
and popMax are only called on a non-empty stack.
"""

from testkit import run


class MaxStack:

    def __init__(self):
        # TODO: your code here
        pass

    def push(self, x: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def peekMax(self) -> int:
        raise NotImplementedError

    def popMax(self) -> int:
        raise NotImplementedError


def run_ops(ops: list) -> list:
    """Make a MaxStack, apply ops like ("push", 5) or ("pop",), return each result."""
    stack = MaxStack()
    return [getattr(stack, name)(*args) for name, *args in ops]


if __name__ == "__main__":
    run(run_ops, [
        (([("push", 5), ("push", 1), ("push", 5), ("top",), ("popMax",), ("top",),
           ("peekMax",), ("pop",), ("top",)],),
         [None, None, None, 5, 5, 1, 5, 1, 5], "official example"),
        (([("push", 1), ("push", 5), ("push", 3), ("push", 5), ("popMax",), ("top",),
           ("popMax",), ("top",), ("pop",), ("top",)],),
         [None, None, None, None, 5, 3, 5, 3, 3, 1], "duplicate max: popMax takes the one nearest the top"),
        (([("push", 9), ("push", 1), ("push", 2), ("popMax",), ("top",), ("peekMax",),
           ("pop",), ("pop",)],),
         [None, None, None, 9, 2, 2, 2, 1], "max is at the bottom"),
        (([("push", 3), ("peekMax",), ("push", 7), ("peekMax",), ("pop",), ("peekMax",)],),
         [None, 3, None, 7, 7, 3], "max goes back down after pop"),
        (([("push", -2), ("push", -5), ("peekMax",), ("popMax",), ("top",)],),
         [None, None, -2, -2, -5], "negative numbers"),
    ])
