class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        sameLableCount = [0 for i in range(n)]

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = set()
        
        def dfs(node):
            visited.add(node)
            if not graph[node]:
                count = dict()
                count[labels[node]] = 1
                sameLableCount[node] = 1
                return count

            newCount = defaultdict(int)
            newCount[labels[node]] += 1
            for child in graph[node]:
                if child in visited:
                    continue

                branch = dfs(child)
                for i in branch.keys():
                    newCount[i] += branch[i]

            sameLableCount[node] = newCount[labels[node]]
            return newCount
            
        dfs(0)
        
        return sameLableCount