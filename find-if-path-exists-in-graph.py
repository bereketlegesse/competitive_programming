class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = disjointSet(n)
        for a,b in edges:
            graph.union(a,b)

        return graph.get(source) == graph.get(destination)
      
class disjointSet:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def get(self, a):
        if a == self.roots[a]:
            return a

        root = self.get(self.roots[a])
        self.roots[a] = root
        return root
    
    def union(self, a, b):
        rootA = self.get(a)
        rootB = self.get(b)
        if rootA == rootB:
            return a,b
            
        if self.rank[rootA] == self.rank[rootB]:
            self.rank[rootA] += 1

        if self.rank[rootA] > self.rank[rootB]:
            self.roots[rootB] =  rootA
            
        else:
            self.roots[rootA] = rootB