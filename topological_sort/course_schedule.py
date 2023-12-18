from collections import *
from typing import List
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = defaultdict(list)
        inDeg = [0]*numCourses
        for c in prerequisites:
            adj[c[0]].append(c[1])
            inDeg[c[1]] += 1
        
        q = deque()
        for i, deg in enumerate(inDeg):
            if deg == 0:
                q.append(i)
        # BFS for topological sort
        # Kahn's Algorithm
        count = 0
        while q:
            c = q.popleft()
            count += 1
            for child in adj[c]:
                inDeg[child] -= 1
                if inDeg[child] == 0:
                    q.append(child)
        return count == numCourses
numCourses = 2
prerequisites = [[1,0]]
sol = Solution()
res = sol.canFinish(numCourses,prerequisites)
print(res)
