class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        totalLength = 0
        n = len(routes)
        for i in range(n):
            totalLength += len(routes[i])
            for city in routes[i]:
                graph[city].append(i)

        queue = deque()
        queue.append(target)
        buses = 1
        visited = set()
        visited.add(target)

        while queue:
            curLen = len(queue)
            
            for _ in range(curLen):
                node = queue.popleft()

                for idx in graph[node]:
                    for child in routes[idx]:
                        if child in visited:
                            continue
                        if child == source:
                            return buses
                        visited.add(child)
                        queue.append(child)
                    
                        if buses > len(routes):
                            return -1

            buses += 1

        return -1