from collections import *
from typing import List
import math

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[], []] for i in range(n)]
        #0 is red, 1 is blue
        for start, end in redEdges:
            graph[start][0].append(end)
        for start, end in blueEdges:
            graph[start][1].append(end)
        #[[last_edge_red, last_edge_grean]]
        dists = [[0, 0]] + [[float("inf"), float("inf")] for i in range(n - 1)]
        #priority queue
        q = [[0, 0], [0, 1]]
        hop = 0
        while q:
            for _ in range(len(q)):
                node, pre_color = q.pop(0)
                for neighbor in graph[node][1-pre_color]:
                    if dists[neighbor][1-pre_color] == float("inf"):
                        dists[neighbor][1-pre_color] = hop + 1
                        q.append([neighbor, 1-pre_color])
            hop += 1
        return [-1 if dist == float("inf") else dist for dist in map(min, dists)]
n = 5
redEdges = [[1,4],[0,3]]
blueEdges = [[3,1],[3,4]]
sol = Solution()
res = sol.shortestAlternatingPaths(n,redEdges,blueEdges)
print(res)


