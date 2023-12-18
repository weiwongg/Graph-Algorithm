from collections import *
from typing import List

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        graph=[]
        for p in range(n):
            for q in range(p+1, n):
                graph.append([p,q,manhattan(points[p], points[q])])
        graph.sort(key=lambda x:x[2])
        
        num = 0
        cost = 0
        uf = UF(n)
        #Kruskal’s algorithm
        for e in graph:
            if num == n-1:
                break
            p,q,w=e
            if not uf.connected(p,q):
                num += 1
                cost += w
                uf.union(p,q)
        return cost


#Ref: https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
class UF:
    def __init__(self,N):
        self.count=N
        self.root=[0]
        self.size=[0]
        for i in range(1,N+1):
            self.root.append(i)
            self.size.append(1)

    def union(self,p,q):
        if self.connected(p,q):
            return;
        p_root=self.find(p)
        q_root=self.find(q)
        if self.size[p_root]<= self.size[q_root]:
            self.root[p_root]=q_root
            self.size[q_root]+=self.size[p_root]
        else:
            self.root[q_root]=self.root[p_root]
            self.size[p_root]=self.size[p_root]
        self.count-=1

    def find(self,p):
        while p!=self.root[p]:
            p=self.root[p]
        return p

    def connected(self,p,q):
        return self.find(p)==self.find(q)

    def count():
        return self.count
        
        
points = [[3,12],[-2,5],[-4,1]]
sol = Solution()
res = sol.minCostConnectPoints(points)
print(res)
