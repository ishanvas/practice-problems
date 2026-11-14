"""LeetCode 994. Rotting Oranges (Medium) - BFS
https://leetcode.com/problems/rotting-oranges/

Each grid cell is 0 (empty), 1 (fresh orange) or 2 (rotten orange).
Every minute, each fresh orange next to a rotten one (up, down, left, right)
becomes rotten. Return the minimum number of minutes until no fresh orange
is left, or -1 if that can never happen.

Constraints: 1 <= rows, cols <= 10.
"""

from testkit import run
from typing import List
from collections import deque

def in_bounds(x, y, n, m) -> bool:
    if x>=0 and x<n and y>=0 and y<m:
        return True
    return False

def oranges_rotting(grid: list[list[int]]) -> int:
    n = len(grid)
    m = len(grid[0])

    visited = set()
    fresh_oranges = 0
    minute = 0
    moves = [(0,1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append([i, j])
                visited.add(tuple([i, j]))
                
            if grid[i][j] == 1:
                fresh_oranges += 1


    while len(queue) > 0 and fresh_oranges > 0:
        
        for _ in range(len(queue)):
            index = queue.popleft()
                

            for move in moves:
                x_new = index[0] + move[0]
                y_new = index[1] + move[1]

                if in_bounds(x_new, y_new, n, m):
                    if tuple([x_new, y_new]) not in visited and grid[x_new][y_new] == 1:
                        queue.append([x_new, y_new])
                        visited.add(tuple([x_new, y_new]))
                        fresh_oranges -= 1
        minute += 1

    return minute  if fresh_oranges ==0 else -1


def oranges_rotting_fixed(grid: list[list[int]]) -> int:
    # Same as oranges_rotting, with 3 changes marked CHANGED.
    n = len(grid)
    m = len(grid[0])

    visited = set()
    fresh_oranges = 0
    minute = 0
    moves = [(0,1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append([i, j])
                visited.add(tuple([i, j]))

            if grid[i][j] == 1:
                fresh_oranges += 1


    while len(queue) > 0 and fresh_oranges > 0:  # CHANGED 1: stop once nothing is fresh

        for _ in range(len(queue)):
            index = queue.popleft()
            # CHANGED 2: removed the decrement here (it ran one level late)

            for move in moves:
                x_new = index[0] + move[0]
                y_new = index[1] + move[1]

                if in_bounds(x_new, y_new, n, m):
                    if tuple([x_new, y_new]) not in visited and grid[x_new][y_new] == 1:
                        queue.append([x_new, y_new])
                        visited.add(tuple([x_new, y_new]))
                        fresh_oranges -= 1  # CHANGED 2: count it the moment it rots
        minute += 1

    return minute  if fresh_oranges == 0 else -1  # CHANGED 3: no more "- 1"


if __name__ == "__main__":

    for fn in [oranges_rotting, oranges_rotting_fixed]:
      run(fn, [
        (([[2, 1, 1], [1, 1, 0], [0, 1, 1]],), 4, "official example 1"),
        (([[2, 1, 1], [0, 1, 1], [1, 0, 1]],), -1, "official example 2: bottom-left never rots"),
        (([[0, 2]],), 0, "official example 3: nothing fresh at the start"),
        (([[0]],), 0, "no oranges at all"),
        (([[1]],), -1, "fresh orange but nothing rotten"),
        (([[2, 1, 1, 1, 2]],), 2, "two rotten oranges spread at the same time"),
    ])
