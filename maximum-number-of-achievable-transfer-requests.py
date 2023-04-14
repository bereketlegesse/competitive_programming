class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        graph = {i:0 for i in range(n)}
        maxRequests = 0
        N = len(requests)

        def backtrack(index, count):
            nonlocal maxRequests
            if index == N:
                if max(graph.values()) == 0 and min(graph.values()) == 0:
                    maxRequests = max(maxRequests, count)
                return
            
            graph[requests[index][0]] -= 1
            graph[requests[index][1]] += 1
            backtrack(index+1, count+1)
            graph[requests[index][0]] += 1
            graph[requests[index][1]] -= 1
            
            backtrack(index+1, count)

        backtrack(0, 0)
        return maxRequests