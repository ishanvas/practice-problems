"""LeetCode 743. Network Delay Time (Medium) - Dijkstra
https://leetcode.com/problems/network-delay-time/

There are n nodes labelled 1 to n. times[i] = [u, v, w] is a directed edge:
a signal takes w time to travel from u to v. A signal is sent from node k.
Return how long it takes for every node to receive it, or -1 if some node
never does.

Constraints: 1 <= n <= 100, 0 <= w <= 100.
"""

from testkit import run
from collections import defaultdict
import heapq

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    minheap = []
    to_nodes = defaultdict(list)

    for u, v, w in times:
        to_nodes[u].append([w, u, v])

    for ele in to_nodes[k]:
        heapq.heappush(minheap, ele)

    nodes_reached = 1
    time_to = {}
    time_to[k] = 0
    visited = set([k])

    while len(minheap) > 0:
        w, u, v = heapq.heappop(minheap)

        if v not in visited:
            time_to[v] = w
            visited.add(v)
            nodes_reached += 1

            for ele in to_nodes[v]:
                if ele[2] not in visited:
                    heapq.heappush(minheap, [time_to[v] + ele[0], ele[1], ele[2]])


    return max(time_to.values()) if nodes_reached == n else -1


        
        
    

    


if __name__ == "__main__":
    run(network_delay_time, [
        (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2, "official example 1"),
        (([[1, 2, 1]], 2, 1), 1, "official example 2"),
        (([[1, 2, 1]], 2, 2), -1, "official example 3: edges are one-way"),
        (([], 1, 1), 0, "single node, nothing to send"),
        (([[1, 2, 10], [1, 3, 1], [3, 2, 1]], 3, 1), 2, "direct edge 1->2 is slower than going via 3"),
        (([[1, 2, 2], [2, 3, 2], [3, 4, 2], [1, 4, 5]], 4, 1), 5, "three short edges add up to more than one long edge"),
        (([[1, 2, 1], [2, 3, 5]], 3, 1), 6, "chain with different edge weights: 1 + 5"),
    ])
