class Solution:
    def convertToList(self, matrix):
        graph = defaultdict(list)
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                if matrix[row][col] == 1:
                    graph[row].append(col)
        return graph

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = self.convertToList(isConnected)
        visited = set()
        count = 0
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)   
        
        for node in graph:
            if node not in visited:
                count += 1
                dfs(node)
        return count