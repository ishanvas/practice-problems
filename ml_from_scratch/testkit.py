"""Shared test runner for the ML practice files. You don't need to edit this."""

import numpy as np


def to_np(x):
    """Turn a torch tensor / list / number into a float64 numpy array."""
    if hasattr(x, "detach"):
        x = x.detach().cpu().numpy()
    return np.asarray(x, dtype=np.float64)


def close(got, want, atol=1e-5, rtol=1e-4, what="value"):
    """Assert got and want have the same shape and are numerically close."""
    g, w = to_np(got), to_np(want)
    assert g.shape == w.shape, f"{what}: shape {g.shape}, want {w.shape}"
    if not np.allclose(g, w, atol=atol, rtol=rtol):
        diff = np.abs(g - w).max()
        raise AssertionError(f"{what}: max abs diff {diff:.3g} (atol={atol})")


def run(title, tests):
    """Run each test and print the results.

    tests: list of (fn, note). Each fn() takes no args and raises
           AssertionError (or anything else) when something is wrong.
    """
    print(f"{title}\n")
    passed = 0
    for fn, note in tests:
        try:
            fn()
            mark, msg = "ok  ", ""
            passed += 1
        except NotImplementedError:
            mark, msg = "TODO", ""
        except AssertionError as e:
            mark, msg = "FAIL", f"  -> {e}"
        except Exception as e:
            mark, msg = "FAIL", f"  -> CRASH {type(e).__name__}: {e}"
        print(f"  {mark} {note}{msg}")
    print(f"\n{passed}/{len(tests)} passed")
