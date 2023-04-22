class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        counter = Counter([(i[0],i[1]) for i in bombs])
        # print(counter)

        for i in range(n):
            x, y, r = bombs[i]
            for j in range(n):
                dist = ((x-bombs[j][0])**2 + (y-bombs[j][1])**2)**(0.5)
                if dist <= r:
                    graph[(x,y)].append((bombs[j][0], bombs[j][1]))

        def dfs(node):
            if node in visited:
                return 0
            count = 1
            visited.add(node)
            for neighbor in graph[node]:
                count += dfs(neighbor)
            return count

        maxCount = 0
        for i in range(n):
            visited = set()
            count = dfs((bombs[i][0], bombs[i][1]))
            count += counter[(bombs[i][0], bombs[i][1])] - 1
            maxCount = max(count, maxCount)
            
        return maxCount