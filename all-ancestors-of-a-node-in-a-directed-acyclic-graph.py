class Solution(object):
    def getAncestors(self, n, edges):
        indegree = [0 for i in range(n)]
        graph = {i:[] for i in range(n)}
        for start,end in edges:
            indegree[end] += 1
            graph[start].append(end)

        queue = deque()
        ancestorList = [set() for _ in range(n)]
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

                ancestorList[child].add(node)
                ancestorList[child].update(ancestorList[node])
        
        ancestorList = [sorted(list(i)) for i in ancestorList]
        return ancestorList