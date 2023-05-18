class Solution(object):
    def minScore(self, n, roads):
        city = disjointSets(n)
        for a, b, score in roads:
            city.union(a-1, b-1, score)

        return city.minEdge()

class disjointSets:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.minEdges = [float("inf") for i in range(n)]

    def get(self, a):
        if a == self.roots[a]:
            return a

        root = self.get(self.roots[a])
        self.roots[a] = root
        return root

    def union(self, a, b, score):
        rootA = self.get(a)
        rootB = self.get(b)
        if rootA == rootB:
            self.minEdges[rootA] = min(self.minEdges[rootA], score)
            return

        if self.rank[rootA] == self.rank[rootB]:
            self.rank[rootA] += 1
            
        if self.rank[rootA] > self.rank[rootB]:
            self.roots[rootB] =  rootA
            self.minEdges[rootA] = min(self.minEdges[rootA],self.minEdges[rootB],score)
        else:
            self.roots[rootA] =  rootB
            self.minEdges[rootB] = min(self.minEdges[rootA],self.minEdges[rootB],score)
    def minEdge(self):
        return self.minEdges[self.get(0)]