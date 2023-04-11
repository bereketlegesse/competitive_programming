class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {i:[] for i in range(1,n+1)}
        for i in dislikes:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        

        colorSet = {}
        def dfs(node, color):
            if node in colorSet:
                return colorSet[node] == color

            colorSet[node] = color
            if node in graph:
                for neighbor in graph[node]:
                    if not dfs(neighbor, 1- color):
                        return False
            return True

        for node in graph:
            if not node in colorSet and not dfs(node, 0):
                return False
                
        return True