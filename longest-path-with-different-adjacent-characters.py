class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        N = len(parent)
        graph = {i:[] for i in range(N)}
        for i in range(1,N):
            graph[parent[i]].append(i)

        maxLen = 0
        def traverse(node):
            nonlocal maxLen
            if len(graph[node]) == 0:
                return [s[node], 1]
            bestPath = [s[node], 1]
            secondPath = [s[node], 1]

            for child in graph[node]:
                prev, length = traverse(child)
                if prev != s[node]:
                    if length >= bestPath[-1]:
                        secondPath[:] = bestPath
                        bestPath = [s[node], length+1]
                    elif secondPath[-1] <= length:
                        secondPath = [s[node], length+1]
                    combinedPath = bestPath[-1] + secondPath[-1] - 1 if secondPath[-1] > 1 else 0
                    maxLen = max(maxLen, combinedPath, bestPath[-1])
            print(node, bestPath, secondPath)
            return bestPath
        bestPath = traverse(0)
        print(maxLen)
        return max(maxLen, bestPath[-1])