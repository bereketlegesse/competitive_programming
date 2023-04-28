class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = defaultdict(list)
        blueGraph = defaultdict(list)
        answer = [None for i in range(n)]
        answer[0] = 0
        distance = 0

        for redEdge in redEdges:
            redGraph[redEdge[0]].append(redEdge[1])
        for  blueEdge in blueEdges:
            blueGraph[blueEdge[0]].append(blueEdge[1])

        queue = deque()
        for child in redGraph[0]:
            queue.append((child,0))
        for child in blueGraph[0]:
            queue.append((child, 1))

        visited = set()
        
        while queue:
            distance += 1 
            curLen = len(queue)

            for _ in range(curLen):
                node,color = queue.popleft()
                if (node, color) in visited:
                    continue

                visited.add((node, color))
                if answer[node] == None:
                    answer[node] = distance
                if color == 0:
                    for child in blueGraph[node]:
                        queue.append((child, 1))
                else:
                    for child in redGraph[node]:
                        queue.append((child, 0))
    
        for i,n in enumerate(answer):
            if n == None:
                answer[i] = -1

        return answer