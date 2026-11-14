"""LeetCode 684. Redundant Connection (Medium) - Union-Find
https://leetcode.com/problems/redundant-connection/

A tree with n nodes (labelled 1 to n) had one extra edge added, so it now has
exactly one cycle. edges lists all n edges. Return an edge you can remove to
get a tree again. If there are several, return the one that appears last
in edges.

Constraints: 3 <= n <= 1000.
"""

from testkit import run

class UnionFind:

    def __init__(self):
        self.array = {}
        self.available_index = 1

    def union(self, a, b) -> False:
        print(f'Union {a} {b}')
        set1 = self.find(a)
        set2 = self.find(b)

        if set1 == -1 or set2 == -1:
            if set1 == -1 and set2 == -1:
                selected = self.available_index;
                self.available_index += 1
            else:
                selected = max(set1, set2)
            
            self.array[a] = selected
            self.array[b] = selected
                
        elif set1 == set2:
            return False
        else:
            self.array[set1] = set2

        print(self.array)
        return True

    def find(self, a):
        if a not in self.array:
            return -1
        
        cur = a
        while self.array[cur] != cur:
            cur = self.array[cur]
        return cur
    


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    # TODO: your code here


    uf = UnionFind()
    redundant_edge = None

    for edge in edges:
        if not uf.union(edge[0], edge[1]):
            redundant_edge = edge

    return redundant_edge
    


if __name__ == "__main__":
    run(find_redundant_connection, [
        (([[1, 2], [1, 3], [2, 3]],), [2, 3], "official example 1"),
        (([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],), [1, 4], "official example 2"),
        (([[1, 2], [2, 3], [3, 1]],), [3, 1], "whole graph is the cycle"),
        (([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]],), [2, 5], "cycle 2-4-3-5 closes on the last edge"),
    ])
