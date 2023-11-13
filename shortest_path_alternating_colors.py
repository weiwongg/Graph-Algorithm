from collections import *
from typing import List
import math

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for frm, to in redEdges: adj[frm].append((to,1))
        for frm, to in blueEdges: adj[frm].append((to,2))
        dists = [math.inf if i!=0 else 0 for i in range(n)]
        que = [(0,0,0)]
        step = 0
        visited = set((0,0))
        while que:
            print(step)
            for _ in range(len(que)):
                node, pre_color, color = que.pop(0)
                visited.add((node,pre_color))
                for nxt_node, nxt_color in adj[node]:
                    if (nxt_node,nxt_color) not in visited:
                        if nxt_color != color or color == 0:
                            que.append((nxt_node,nxt_color,nxt_color))
                            if dists[nxt_node] > step + 1: dists[nxt_node] = step + 1
            step += 1
        dists = [-1 if dist == math.inf else dist for dist in dists]
        return dists
        
n = 5
redEdges = [[1,4],[0,3]]
blueEdges = [[3,1],[3,4]]
sol = Solution()
res = sol.shortestAlternatingPaths(n,redEdges,blueEdges)
print(res)


