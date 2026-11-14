"""LeetCode 210. Course Schedule II (Medium) - topological sort
https://leetcode.com/problems/course-schedule-ii/

There are num_courses courses labelled 0 to num_courses - 1.
prerequisites[i] = [a, b] means you must take course b before course a.
Return any order that lets you take every course, or [] if it's impossible.

Constraints: 1 <= num_courses <= 2000.
"""

from testkit import run
from collections import defaultdict, deque


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:

    preq_map = defaultdict(set)
    
    
    for req in prerequisites:
        #b req[1] before a req[0]
        preq_map[req[0]].add(req[1])

    stack = []
    order = []
    
    satisfied = set()

    for i in range(num_courses):
        if i  in satisfied:
            continue
        visited = set()
        stack.append((i, 0))
        visited.add(i)

        while len(stack) > 0:
            index, seen_before = stack.pop()

            if seen_before == 0 and index in satisfied:
                continue

            if seen_before == 1:
                satisfied.add(index)
                order.append(index)
                visited.remove(index)
            else:
                stack.append((index, 1))
                visited.add(index)
                for dep in preq_map[index]:
                    if dep in visited:
                        return []

                    if dep not in satisfied:
                        stack.append((dep, 0))
                        

    return order


def find_order_clean(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    # Same algorithm as find_order: iterative DFS from each course down to its
    # prerequisites, recording a course once all of its prerequisites are recorded.
    prereqs = defaultdict(set)
    for course, before in prerequisites:
        prereqs[course].add(before)

    order = []
    done = set()     # already recorded in order
    on_path = set()  # being explored right now; reaching one again means a cycle

    for start in range(num_courses):
        stack = [(start, False)]  # (course, finished): False = explore it, True = record it
        while stack:
            course, finished = stack.pop()
            if finished:
                on_path.remove(course)
                done.add(course)
                order.append(course)
            elif course not in done:  # also skips outdated copies and finished start courses
                on_path.add(course)
                stack.append((course, True))
                for before in prereqs[course]:
                    if before in on_path:
                        return []
                    if before not in done:
                        stack.append((before, False))

    return order








def valid(got, want, args):
    """Many orders can be correct, so check the rules instead of one exact answer."""
    n, prereqs = args
    if want == []:
        return got == []
    if sorted(got) != list(range(n)):
        return False
    pos = {course: i for i, course in enumerate(got)}
    return all(pos[b] < pos[a] for a, b in prereqs)


ANY = "any valid order"

if __name__ == "__main__":
  for fn in [find_order, find_order_clean]:
    run(fn, [
        ((2, [[1, 0]]), ANY, "official example 1: [0, 1]"),
        ((4, [[1, 0], [2, 0], [3, 1], [3, 2]]), ANY, "official example 2: [0,1,2,3] or [0,2,1,3]"),
        ((1, []), ANY, "official example 3: [0]"),
        ((3, []), ANY, "no prerequisites, any order works"),
        ((2, [[1, 0], [0, 1]]), [], "two courses need each other"),
        ((3, [[0, 1], [1, 2], [2, 1]]), [], "cycle between 1 and 2"),
        ((3, [[0, 1], [0, 2], [2, 1]]), ANY, "no cycle: 0 needs 1 and 2, and 2 also needs 1"),
    ], check=valid)
