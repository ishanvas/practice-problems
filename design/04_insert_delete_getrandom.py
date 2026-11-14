"""LeetCode 380. Insert Delete GetRandom O(1) (Medium) - Design (list + index map)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a set with average O(1) time for every call.

  insert(val)  add val if it isn't there. Return True if it was added.
  remove(val)  remove val if it's there. Return True if it was removed.
  getRandom()  return a random element, each one equally likely.

This is the warm-up for 02_insert_delete_getrandom_duplicates.py.

Constraints: -2^31 <= val <= 2^31 - 1, at most 2 * 10^5 calls, and getRandom
is only called when the set isn't empty.

Testing note: a ("getRandom",) step gives the sorted distinct values seen
over many draws, and a ("share", v) step gives the fraction of draws equal to
v, rounded to 1 decimal. "share" is only for the tests.
"""

from testkit import run


class RandomizedSet:

    def __init__(self):
        # TODO: your code here
        pass

    def insert(self, val: int) -> bool:
        raise NotImplementedError

    def remove(self, val: int) -> bool:
        raise NotImplementedError

    def getRandom(self) -> int:
        raise NotImplementedError


DRAWS = 20000


def run_ops(ops: list) -> list:
    """Make a RandomizedSet, apply ops like ("insert", 1), return each result."""
    rs = RandomizedSet()
    out = []
    for name, *args in ops:
        if name == "getRandom":
            out.append(sorted({rs.getRandom() for _ in range(DRAWS)}))
        elif name == "share":
            hits = sum(rs.getRandom() == args[0] for _ in range(DRAWS))
            out.append(round(hits / DRAWS, 1))
        else:
            out.append(getattr(rs, name)(*args))
    return out


if __name__ == "__main__":
    run(run_ops, [
        (([("insert", 1), ("remove", 2), ("insert", 2), ("getRandom",), ("remove", 1),
           ("insert", 2), ("getRandom",)],),
         [True, False, True, [1, 2], True, False, [2]], "official example"),
        (([("insert", 0), ("insert", 1), ("remove", 0), ("insert", 2), ("remove", 1),
           ("getRandom",)],),
         [True, True, True, True, True, [2]], "removing swaps the last element into the gap"),
        (([("insert", 3), ("remove", 3), ("remove", 3), ("insert", 3), ("getRandom",)],),
         [True, True, False, True, [3]], "remove the only element, then re-add it"),
        (([("insert", 1), ("insert", 2), ("insert", 3), ("insert", 4), ("insert", 5),
           ("share", 3)],),
         [True, True, True, True, True, 0.2], "each element equally likely"),
    ])
