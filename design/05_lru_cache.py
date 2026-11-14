"""LeetCode 146. LRU Cache (Medium) - Design (hash map + doubly linked list)
https://leetcode.com/problems/lru-cache/

Design a least-recently-used cache with a fixed capacity.

  get(key)         return the value for key, or -1 if it's missing. Counts as a use.
  put(key, value)  set or update key. Counts as a use. If this goes over
                   capacity, first evict the least recently used key.

Both must run in O(1) average time. Try it without OrderedDict first.

Constraints: 1 <= capacity <= 3000, 0 <= key <= 10^4, 0 <= value <= 10^5,
at most 2 * 10^5 calls.
"""

from testkit import run


class LRUCache:

    def __init__(self, capacity: int):
        # TODO: your code here
        pass

    def get(self, key: int) -> int:
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        raise NotImplementedError


def run_ops(capacity: int, ops: list) -> list:
    """Make an LRUCache, apply ops like ("put", 1, 1) or ("get", 1), return each result."""
    cache = LRUCache(capacity)
    return [getattr(cache, name)(*args) for name, *args in ops]


if __name__ == "__main__":
    run(run_ops, [
        ((2, [("put", 1, 1), ("put", 2, 2), ("get", 1), ("put", 3, 3), ("get", 2),
              ("put", 4, 4), ("get", 1), ("get", 3), ("get", 4)]),
         [None, None, 1, None, -1, None, -1, 3, 4], "official example"),
        ((2, [("put", 1, 1), ("put", 2, 2), ("put", 1, 10), ("put", 3, 3), ("get", 2),
              ("get", 1)]),
         [None, None, None, None, -1, 10], "updating a key also makes it recent"),
        ((2, [("put", 1, 1), ("put", 1, 2), ("put", 2, 3), ("get", 1), ("get", 2)]),
         [None, None, None, 2, 3], "updating an existing key must not evict anything"),
        ((1, [("put", 1, 1), ("put", 2, 2), ("get", 1), ("get", 2)]),
         [None, None, -1, 2], "capacity 1"),
        ((2, [("get", 5), ("put", 5, 0), ("get", 5)]),
         [-1, None, 0], "missing key, and a stored value of 0"),
    ])
