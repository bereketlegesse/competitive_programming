class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        status = dict()     # 0-> is being processed 1-> safeNode
        safeNodes = []
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

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

        for node in range(numCourses):
            dfs(node)

        for node in status:
            if status[node] == 1:
                safeNodes.append(node)

        return len(safeNodes) == numCourses