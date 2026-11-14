"""LeetCode 489. Robot Room Cleaner (Hard) - Backtracking DFS
https://leetcode.com/problems/robot-room-cleaner/

A robot is somewhere in a room you can't see. Clean every cell it can reach,
using only this API:

  robot.move()       try to step forward one cell. Returns True if it moved,
                     False if a wall or blocked cell is in the way.
  robot.turnLeft()   turn 90 degrees left, staying in the same cell
  robot.turnRight()  turn 90 degrees right
  robot.clean()      clean the current cell

The robot starts facing up. You don't know the room's layout or where the
robot starts. Treat the start as (0, 0) and track positions relative to it.

Hint: after visiting a neighbour, bring the robot back to where it was and
face it the same way (turn around, move, turn around again).

Constraints: the room is at most 100 x 100, and the start is an open cell.
"""

from testkit import run


def clean_room(robot: "Robot") -> None:
    # TODO: your code here
    raise NotImplementedError


class Robot:
    """Test double for the hidden robot. room[r][c] is 1 if open, 0 if blocked."""

    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

    def __init__(self, room, row, col, max_steps=200_000):
        self._room, self._r, self._c, self._d = room, row, col, 0
        self._steps, self._max_steps = 0, max_steps
        self.cleaned = set()

    def _tick(self):
        self._steps += 1
        if self._steps > self._max_steps:
            raise RuntimeError("too many robot calls - probably looping forever")

    def move(self) -> bool:
        self._tick()
        dr, dc = self.DIRS[self._d]
        r, c = self._r + dr, self._c + dc
        if 0 <= r < len(self._room) and 0 <= c < len(self._room[0]) and self._room[r][c] == 1:
            self._r, self._c = r, c
            return True
        return False

    def turnLeft(self) -> None:
        self._tick()
        self._d = (self._d - 1) % 4

    def turnRight(self) -> None:
        self._tick()
        self._d = (self._d + 1) % 4

    def clean(self) -> None:
        self._tick()
        self.cleaned.add((self._r, self._c))


def solve(room: list[list[int]], row: int, col: int) -> int:
    """Run clean_room and return how many cells got cleaned."""
    robot = Robot(room, row, col)
    clean_room(robot)
    return len(robot.cleaned)


if __name__ == "__main__":
    official = [
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]
    run(solve, [
        ((official, 1, 3), 30, "official example 1"),
        (([[1]], 0, 0), 1, "official example 2: one cell"),
        (([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 2, 2), 8, "ring around a pillar"),
        (([[1, 1, 0, 1], [1, 1, 0, 1]], 0, 0), 4, "the right side is walled off"),
        (([[1, 0, 1], [1, 1, 1], [0, 1, 0]], 2, 1), 6, "start at the bottom, facing up"),
        (([[1] * 6 for _ in range(6)], 3, 3), 36, "open 6x6 room"),
    ])
