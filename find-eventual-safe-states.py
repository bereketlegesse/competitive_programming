class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        status = dict()     # 0-> is being processed 1-> safeNode
        safeNodes = []
        n = len(graph)
        def dfs(node):
            if node in status:
                return status[node] == 1
            status[node] = 0
            safe = True
            for child in graph[node]:
                if not dfs(child):
                    safe = False
            if safe:
                status[node] = 1

            return safe == True

        for node in range(n):
            dfs(node)

        for node in status:
            if status[node] == 1:
                safeNodes.append(node)

        return sorted(safeNodes)