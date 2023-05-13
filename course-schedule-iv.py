class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        incomingEdges = [0 for i in range(numCourses)]
        graph = {i:[] for i in range(numCourses)}
        ancestors = [set() for _ in range(numCourses)]
        answer = []

        for pre,course in prerequisites:
            incomingEdges[course] += 1
            graph[pre].append(course)

        queue = deque()
        for i,n in enumerate(incomingEdges):
            if n == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                ancestors[child].add(node)
                ancestors[child].update(ancestors[node])
                incomingEdges[child] -= 1
                
                if incomingEdges[child] == 0:
                    queue.append(child)
        
        for u,v in queries:
            if u in ancestors[v]:
                answer.append(True)
            else:
                answer.append(False)

        return answer