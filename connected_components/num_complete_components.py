from collections import *
from typing import List
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        for src, trg in edges:
            adj[src].append(trg)
            adj[trg].append(src)
        remaining = set([i for i in range(n)])
        comp = set()
        #depth-first search
        def dfs(i):
            comp.add(i)
            remaining.discard(i)
            for node in adj[i]:
                if node not in comp:
                    comp.add(node)
                    remaining.discard(node)
                    dfs(node)
        num = 0
        while remaining:
            #find one connected component each time
            #empty component
            comp = set()
            i = min(remaining)
            dfs(i)
            for node in comp:
                if len(adj[node]) != len(comp)-1:
                    num -= 1
                    break
            num += 1
        return num
        
n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]
sol = Solution()
res = sol.countCompleteComponents(n,edges)
print(res)
