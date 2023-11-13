from collections import *
from typing import List
from heapq import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for frm, to, cst in flights:
            adj[frm].append((cst, to))
        que = [(0,0,src)]
        dists = [float("infinity") if i!=src else 0 for i in range(n)]
        hops = [float("infinity") if i!=src else 0 for i in range(n)]
        while que:
            min_cst, hop, x = heappop(que)
            if x == dst: return (dists[dst],hops[dst])
            for cst, to in adj[x]:
                if dists[to] > min_cst + cst:
                    dists[to] = min_cst + cst
                    hops[to] = hop + 1
                    heappush(que, (dists[to],hops[to],to))
        return ("inf", None)
        
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
sol = Solution()
res = sol.findCheapestPrice(n,flights,src,dst,k)
print(res)


