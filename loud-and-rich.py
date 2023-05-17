class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = {i:[] for i in range(n)}
        incomingEdges = [0 for i in range(n)]

        for r,p in richer:
            graph[r].append(p)
            incomingEdges[p] += 1
        
        queue = deque()
        ancestors = [{i} for i in range(n)]
        for i in range(n):
            if incomingEdges[i] == 0:
                queue.append(i)
        while queue:
            cur = queue.popleft()
            for child in graph[cur]:
                ancestors[child].update(ancestors[cur])
                incomingEdges[child] -= 1
                if incomingEdges[child] == 0:
                    queue.append(child)

        answer = []
        for i in ancestors:
            quietest = min(i, key = lambda x:quiet[x])
            answer.append(quietest)
            
        return answer