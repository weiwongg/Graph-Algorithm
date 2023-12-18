from collections import *
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for frm, to, cst in flights:
            adj[frm].append((cst, to))
        dists = [float("infinity") if i!=src else 0 for i in range(n)]
        q = deque([(src, 0)])
        for _ in range(k+1):
            for _ in range(len(q)):
                x,curCst=q.popleft()
                for cst, leaf in adj[x]:
                    if cst + curCst < dists[leaf]:
                        dists[leaf] = cst + curCst
                        q.append((leaf,dists[leaf]))
        return -1 if dists[dst]==float("infinity") else dists[dst]
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
sol = Solution()
res = sol.findCheapestPrice(n,flights,src,dst,k)
print(res)
