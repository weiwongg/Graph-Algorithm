from collections import *
from typing import List
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        adj=defaultdict(list)
        for i,j in dislikes:
            adj[i-1].append(j-1)
            adj[j-1].append(i-1)
        visited = set()
        def bfs(i):
            q = deque()
            q.append(i)
            colors = defaultdict(list)
            colors[i]=0
            while q:
                node = q.popleft()
                visited.add(node)
                for child in adj[node]:
                    if child not in visited:
                        colors[child] = 1-colors[node]
                        q.append(child)
                    elif colors[child] == colors[node]:
                        return False
            return True

        for i in range(n):
            if i not in visited:
                if not bfs(i):
                    return False
        return True
n = 4
dislikes = [[1,2],[1,3],[2,4]]
sol = Solution()
res = sol.possibleBipartition(n,dislikes)
print(res)
