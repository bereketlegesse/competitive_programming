class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        N = len(edges)
        cycleLength = -1

        graph = {i:[] for i in range(N)}
        for i,n in enumerate(edges):
            if n != -1:
                graph[i].append(n)
  
        def dfs(node, idx):
            if node in index:
                return idx - index[node]
            
            if node in visited:
                return -1
                
            index[node] = idx
            cycle = -1
            visited.add(node)
            if len(graph[node]) != 0:
                child = graph[node][0]
                cycle = max(dfs(child, idx + 1), -1)

            return cycle
        
        for i in range(N):
            index = dict()
            if i not in visited:
                length = dfs(i,1)
                cycleLength = max(cycleLength, length)
                

        return cycleLength