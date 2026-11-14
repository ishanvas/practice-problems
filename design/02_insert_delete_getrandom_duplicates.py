"""LeetCode 381. Insert Delete GetRandom O(1) - Duplicates allowed (Hard) - Design (list + index sets)
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

Design a multiset with average O(1) time for every call.

  insert(val)  add val. Return True if val wasn't there before, else False.
  remove(val)  remove one copy of val. Return True if val was there.
  getRandom()  return a random element. Each element's chance is proportional
               to how many copies of it there are.

Constraints: -2^31 <= val <= 2^31 - 1, at most 2 * 10^5 calls, and getRandom
is only called when the collection isn't empty.

Testing note: random results can't be compared directly, so run_ops calls
getRandom many times. A ("getRandom",) step gives the sorted distinct values
it saw, and a ("share", v) step gives the fraction of draws equal to v,
rounded to 1 decimal. "share" is only for the tests; don't add it to the class.
"""

from testkit import run


class RandomizedCollection:

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
    """Make a RandomizedCollection, apply ops like ("insert", 1), return each result."""
    rc = RandomizedCollection()
    out = []
    for name, *args in ops:
        if name == "getRandom":
            out.append(sorted({rc.getRandom() for _ in range(DRAWS)}))
        elif name == "share":
            hits = sum(rc.getRandom() == args[0] for _ in range(DRAWS))
            out.append(round(hits / DRAWS, 1))
        else:
            out.append(getattr(rc, name)(*args))
    return out


if __name__ == "__main__":
    run(run_ops, [
        (([("insert", 1), ("insert", 1), ("insert", 2), ("getRandom",), ("remove", 1),
           ("getRandom",)],),
         [True, False, True, [1, 2], True, [1, 2]], "official example"),
        (([("remove", 5), ("insert", 5), ("remove", 5), ("remove", 5), ("insert", 5),
           ("getRandom",)],),
         [False, True, True, False, True, [5]], "remove a missing value, then re-add it"),
        (([("insert", 4), ("insert", 3), ("insert", 4), ("insert", 2), ("insert", 4),
           ("remove", 4), ("remove", 3), ("remove", 4), ("getRandom",), ("remove", 4),
           ("getRandom",)],),
         [True, True, False, True, False, True, True, True, [2, 4], True, [2]],
         "removing swaps in the last element, which may be the same value"),
        (([("insert", 1), ("insert", 1), ("insert", 1), ("insert", 1), ("insert", 2),
           ("share", 1), ("remove", 1), ("remove", 1), ("share", 1)],),
         [True, False, False, False, True, 0.8, True, True, 0.7],
         "chance follows the counts: 4/5, then 2/3"),
        (([("insert", 10), ("remove", 10), ("insert", 20), ("getRandom",)],),
         [True, True, True, [20]], "removing the only element"),
    ])
