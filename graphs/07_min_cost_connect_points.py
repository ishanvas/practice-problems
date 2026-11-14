"""LeetCode 1584. Min Cost to Connect All Points (Medium) - minimum spanning tree
https://leetcode.com/problems/min-cost-to-connect-all-points/

points[i] = [x, y]. The cost of connecting two points is their Manhattan
distance, |x1 - x2| + |y1 - y2|. Return the minimum total cost to connect all
points, so that there's exactly one path between any two of them.

Constraints: 1 <= len(points) <= 1000, -10^6 <= x, y <= 10^6.
"""

from testkit import run
import heapq
import math


class UnionFind:

    def __init__(self, n):
        self.array = [i for i in range(n)]

    def union(self, a, b) -> bool:
        set1 = self.find(a)
        set2 = self.find(b)

        if set1 == set2:
            return False
        self.array[set2] = set1

        return True


    def find(self, a):
        cur = a
        while self.array[cur] != cur:
            cur = self.array[cur]
        return cur

    def find_compressed(self, a):
        # Same as find, but afterwards every node on the path points
        # straight at the root, so the next call on any of them is one step.
        root = a
        while self.array[root] != root:
            root = self.array[root]
        while self.array[a] != root:  # second pass: re-point the path
            self.array[a], a = root, self.array[a]
        return root

    def union_by_size(self, a, b) -> bool:
        # Same as union, but the smaller group goes under the larger one,
        # so no tree gets deeper than about log2(n).
        if not hasattr(self, "size"):
            self.size = [1] * len(self.array)
        root_a = self.find_compressed(a)
        root_b = self.find_compressed(b)
        if root_a == root_b:
            return False
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.array[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True

        

def cal_manhat_dist(x:list[int], y:list[int]):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def min_cost_connect_points(points: list[list[int]]) -> int:
    # TODO: your code here
    
    min_heap = []
    num_points  = len(points)

    for i in range(num_points):
        for j in range(i+1, num_points):
            dist = cal_manhat_dist(points[i], points[j])
            heapq.heappush(min_heap, [dist, i, j])

    # iterate over all the points and pick until all points are picked

    cost = 0
    union_find = UnionFind(num_points)
    picked = 0

    while len(min_heap) > 0:
        dist, u, v = heapq.heappop(min_heap)
        if union_find.union(u, v):
            cost += dist
            picked += 1
        if picked == num_points -1:
            break
        

    return cost


class PrimMST:
    """Prim's algorithm with a plain array: O(n^2) time, O(n) memory, no heap."""

    def min_cost_prim(self, points: list[list[int]]) -> int:
        n = len(points)
        INF = float("inf")
        best = [INF] * n      # best[i]: cheapest edge from the tree to point i so far
        in_tree = [False] * n
        best[0] = 0           # start the tree at point 0 (any point works)
        cost = 0

        for _ in range(n):
            # 1. Pick the cheapest point not yet in the tree: O(n).
            u = -1
            for i in range(n):
                if not in_tree[i] and (u == -1 or best[i] < best[u]):
                    u = i

            # 2. Add it; best[u] is the edge that connects it to the tree.
            in_tree[u] = True
            cost += best[u]

            # 3. u may give the remaining points a cheaper connection: O(n).
            for v in range(n):
                if not in_tree[v]:
                    d = cal_manhat_dist(points[u], points[v])
                    if d < best[v]:
                        best[v] = d

        return cost


if __name__ == "__main__":
  for fn in [min_cost_connect_points, PrimMST().min_cost_prim]:
    run(fn, [
        (([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],), 20, "official example 1"),
        (([[3, 12], [-2, 5], [-4, 1]],), 18, "official example 2"),
        (([[0, 0], [1, 1], [1, 0], [-1, 1]],), 4, "official example 3"),
        (([[0, 0]],), 0, "one point, nothing to connect"),
        (([[-1000000, -1000000], [1000000, 1000000]],), 4000000, "largest coordinates"),
        (([[0, 0], [0, 1], [10, 0], [10, 1]],), 12, "two close pairs far apart: the pairs must still be joined"),
    ])
