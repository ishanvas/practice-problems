"""Find which outcome owns ticket t.

Outcome i owns weights[i] consecutive tickets in the range [0, sum(weights) - 1].
Example: weights = [1, 3, 2]
    ticket: 0 | 1 2 3 | 4 5
    owner:  0 |   1   |  2
"""

import math
import random

def bisect_left(values: list[int], target: int) -> int:

    high = len(values)
    low = 0
    
    while low < high:
        #print(f'low {low} high {high}')
        mid = int((high + low)/2)
        mid_val = values[mid]
        #print(f'mid {mid} and mid_val {mid_val}')

        if target <= mid_val:
            if mid == 0 or target > values[mid-1]:
                return mid
            else:
                high = mid
        else:
            low = mid + 1 

    return -1
     


def find_owner(weights: list[int], t: int) -> int:

    # generate cumulative sum
    csum = [0]* len(weights)
    csum[0] = weights[0]
    
    for i in range(0, len(weights)):
        csum[i] = csum[i-1] + weights[i]

    target = t + 1

    """
    for i in range(0, len(weights)):
        if t < csum[i]:
            return i
    """

    return bisect_left(csum, target)

# ---------------------------------------------------------------------------
# Tests below. Click the run button to run them.
# ---------------------------------------------------------------------------

def brute_force(weights: list[int], t: int) -> int:
    """Slow but obviously correct: walk through the tickets one outcome at a time."""
    for i, w in enumerate(weights):
        if t < w:
            return i
        t -= w
    raise ValueError("ticket out of range")


def check(weights: list[int], t: int, want: int, note: str = "", log: bool = True) -> bool:
    """Run one case, print it, and return True if it passed."""
    got = find_owner(weights, t)
    ok = got == want
    if log or not ok:
        mark = "ok  " if ok else "FAIL"
        extra = f"  # {note}" if note else ""
        print(f"    {mark} weights={weights} t={t} -> got {got}, want {want}{extra}")
    return ok


def test_examples():
    w = [1, 3, 2]
    return [check(w, t, want) for t, want in enumerate([0, 1, 1, 1, 2, 2])]


def test_single_outcome():
    return [check([5], t, 0) for t in range(5)]


def test_zero_weights():
    # Zero-weight outcomes own no tickets, so they must never be returned.
    w = [0, 2, 0, 3, 0]
    results = [check(w, t, want) for t, want in enumerate([1, 1, 3, 3, 3])]
    results.append(check([0, 0, 1], 0, 2, "only the last outcome has tickets"))
    return results


def test_boundaries():
    w = [4, 1, 7]
    return [
        check(w, 0, 0, "first ticket"),
        check(w, 3, 0, "last ticket of outcome 0"),
        check(w, 4, 1, "outcome 1's only ticket"),
        check(w, 5, 2, "first ticket of outcome 2"),
        check(w, 11, 2, "last ticket overall"),
    ]


def test_random_against_brute_force():
    # Too many cases to print them all, so only failures are logged.
    rng = random.Random(0)
    results = []
    for _ in range(500):
        w = [rng.randint(0, 5) for _ in range(rng.randint(1, 10))]
        if sum(w) == 0:
            continue
        for t in range(sum(w)):
            results.append(check(w, t, brute_force(w, t), log=False))
            if results.count(False) >= 10:
                print("    ... stopping after 10 failures")
                return results
    return results


def chi_square_p_value(stat: float, df: int) -> float:
    """Approximate p-value for a chi-square statistic (Wilson-Hilferty), no scipy needed."""
    z = ((stat / df) ** (1 / 3) - (1 - 2 / (9 * df))) / math.sqrt(2 / (9 * df))
    return 0.5 * math.erfc(z / math.sqrt(2))


def test_sampling_distribution():
    # Draw random tickets many times and check each outcome comes up in proportion
    # to its weight, using a chi-square goodness-of-fit test.
    # p-value = chance of a gap this big if sampling is correct; we fail below 0.001.
    rng = random.Random(42)
    n = 100_000
    results = []
    for w in [[1, 3, 2], [10, 1, 1, 1], [0, 5, 0, 5, 1], [1] * 8]:
        total = sum(w)
        counts = [0] * len(w)
        for _ in range(n):
            counts[find_owner(w, rng.randrange(total))] += 1

        print(f"    weights={w}, {n:,} draws")
        print(f"      {'idx':>3} {'weight':>6} {'expected':>9} {'observed':>9}")
        stat = 0.0
        for i, (wi, obs) in enumerate(zip(w, counts)):
            exp = n * wi / total
            print(f"      {i:>3} {wi:>6} {exp:>9.0f} {obs:>9}")
            if wi > 0:
                stat += (obs - exp) ** 2 / exp

        df = sum(wi > 0 for wi in w) - 1
        zero_ok = all(c == 0 for wi, c in zip(w, counts) if wi == 0)
        p = chi_square_p_value(stat, df) if df > 0 else 1.0
        ok = p > 0.001 and zero_ok
        note = "" if zero_ok else ", zero-weight outcome was sampled!"
        print(f"      {'ok  ' if ok else 'FAIL'} chi2={stat:.2f} df={df} p={p:.3f}{note}")
        results.append(ok)
    return results


if __name__ == "__main__":
    tests = [test_examples, test_single_outcome, test_zero_weights,
             test_boundaries, test_random_against_brute_force, test_sampling_distribution]
    passed = 0
    for test in tests:
        print(f"\n{test.__name__}")
        try:
            results = test()
        except NotImplementedError:
            print("  TODO  find_owner not written yet")
            continue
        except Exception as e:
            print(f"  CRASH  {type(e).__name__}: {e}")
            continue
        n_ok = sum(results)
        status = "PASS" if n_ok == len(results) else "FAIL"
        print(f"  {status}  {n_ok}/{len(results)} cases")
        passed += status == "PASS"
    print(f"\n{passed}/{len(tests)} tests passed")
