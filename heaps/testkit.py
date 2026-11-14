"""Shared test runner for the practice files. You don't need to edit this."""

import copy


def run(fn, cases, check=None):
    """Run fn on each case and print the results.

    cases: list of (args, want, note). args is a tuple passed to fn.
    check: optional check(got, want, args) -> bool, for problems where
           more than one answer is correct. Default is got == want.
    """
    print(f"{fn.__name__}\n")
    passed = 0
    for args, want, note in cases:
        shown = ", ".join(repr(a) for a in args)
        try:
            got = fn(*copy.deepcopy(args))  # copy so in-place edits don't change the log
            ok = check(got, want, args) if check else got == want
        except NotImplementedError:
            print("  TODO  write the function first")
            return
        except Exception as e:
            got, ok = f"CRASH {type(e).__name__}: {e}", False
        passed += ok
        mark = "ok  " if ok else "FAIL"
        extra = f"  # {note}" if note else ""
        print(f"  {mark} ({shown}) -> got {got!r}, want {want!r}{extra}")
    print(f"\n{passed}/{len(cases)} passed")
