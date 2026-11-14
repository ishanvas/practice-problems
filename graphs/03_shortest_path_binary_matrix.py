"""LeetCode 1091. Shortest Path in Binary Matrix (Medium) - shortest path (unweighted)
https://leetcode.com/problems/shortest-path-in-binary-matrix/

In an n x n grid, 0 is open and 1 is blocked. Find the shortest path from
the top-left cell to the bottom-right cell, moving through open cells in any
of the 8 directions (including diagonals). The path length is the number of
cells visited, including the start and end. Return -1 if there's no path.

Constraints: 1 <= n <= 100.
"""

from testkit import run
from collections import deque

def is_in_bound(x, y, n, m) -> bool:
    if x>=0 and x< n and y>=0 and y< m:
        return True
    return False



def shortest_path_binary_matrix(grid: list[list[int]]) -> int:

    n = len(grid)
    m = len(grid[0])

    queue = deque([])
    if grid[0][0] == 1:
        return -1

    queue.append([0,0])
    visited  = set()
    visited.add(tuple([0,0]))
    moves = [(1,0), (-1, 0), (0,1), (0,1), (0,-1), (1,1), (-1,-1), (1, -1), (-1, 1)]
    steps  = 1
    

    while len(queue) > 0:

        for _ in range(len(queue)):
            index = queue.popleft()
            if index[0] == n-1 and index[1] == m-1:
                return steps

            for move in moves:
                x_new = index[0] + move[0]
                y_new = index[1] + move[1]
                neighbor =[x_new, y_new]
                if is_in_bound(x_new, y_new, n, m) and tuple(neighbor) not in visited and grid[x_new][y_new] == 0:
                    queue.append(neighbor)
                    visited.add(tuple(neighbor))
        steps += 1

    return -1


# All 8 neighbours: every (dr, dc) combination except staying put.
MOVES = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]


def shortest_path_binary_matrix_clean(grid: list[list[int]]) -> int:
    # Same algorithm: level-by-level BFS from the top-left, counting cells.
    n = len(grid)  # the grid is n x n
    if grid[0][0] == 1:
        return -1

    queue = deque([(0, 0)])
    visited = {(0, 0)}
    steps = 1

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if (r, c) == (n - 1, n - 1):
                return steps
            for dr, dc in MOVES:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        steps += 1

    return -1


if __name__ == "__main__":
  for fn in [shortest_path_binary_matrix, shortest_path_binary_matrix_clean]:
    run(fn, [
        (([[0, 1], [1, 0]],), 2, "official example 1: one diagonal step"),
        (([[0, 0, 0], [1, 1, 0], [1, 1, 0]],), 4, "official example 2"),
        (([[1, 0, 0], [1, 1, 0], [1, 1, 0]],), -1, "official example 3: start is blocked"),
        (([[0]],), 1, "start is the end"),
        (([[0, 0], [0, 1]],), -1, "end is blocked"),
        (([[0, 0, 0], [0, 0, 0], [0, 0, 0]],), 3, "open grid: straight down the diagonal"),
    ])
