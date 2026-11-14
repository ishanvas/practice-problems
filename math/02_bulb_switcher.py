"""LeetCode 319. Bulb Switcher (Medium) - Math (divisor counting)
https://leetcode.com/problems/bulb-switcher/

n bulbs start off. Round 1 turns every bulb on. Round 2 toggles every 2nd
bulb, round 3 every 3rd bulb, and so on. Round i toggles every ith bulb, up
to round n. Return how many bulbs are on after n rounds.

Hint: bulb k is toggled once per divisor of k. Which numbers have an odd
number of divisors?

Constraints: 0 <= n <= 10^9.
"""

from testkit import run


def bulb_switch(n: int) -> int:
    # TODO: your code here
    raise NotImplementedError


if __name__ == "__main__":
    run(bulb_switch, [
        ((3,), 1, "official example 1"),
        ((0,), 0, "official example 2"),
        ((1,), 1, "official example 3"),
        ((4,), 2, "bulbs 1 and 4"),
        ((99,), 9, "just below 100"),
        ((100,), 10, "exactly a square"),
        ((10**9,), 31622, "too big to simulate"),
    ])
