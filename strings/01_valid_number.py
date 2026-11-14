"""LeetCode 65. Valid Number (Hard) - String parsing / state machine
https://leetcode.com/problems/valid-number/

Return whether s is a valid number. A valid number is an integer or a
decimal, optionally followed by an exponent.

  integer:   optional sign (+ or -), then one or more digits
  decimal:   optional sign, then one of: digits "." | digits "." digits | "." digits
  exponent:  "e" or "E", then an integer

So "2", "0089", "-0.1", "4.", "-.9", "2e10" and "-90E3" are valid, and
"abc", "1e", "e3", "99e2.5", "--6" and "95a54e53" are not.

Constraints: 1 <= len(s) <= 20, s has only letters, digits, "+", "-" and ".".
"""

from testkit import run


def is_number(s: str) -> bool:
    # TODO: your code here
    raise NotImplementedError


VALID = ["0", "2", "0089", "-0.1", "+3.14", "4.", "-.9", ".1", "2e10", "-90E3",
         "3e+7", "+6e-1", "53.5e93", "-123.456e789", "1E-0"]
INVALID = ["e", ".", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53",
           "+", "+.", ".e1", "4e+", "1e2e3", "1.2.3", "+-e"]

if __name__ == "__main__":
    run(is_number, [((s,), True, "") for s in VALID] + [((s,), False, "") for s in INVALID])
