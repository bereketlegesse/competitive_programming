class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        newStr = disjointSets(n)

        for a,b in pairs:
            newStr.union(a, b)

        groups = defaultdict(list)
        ans = [None for _ in range(n)]

        for i in range(n):
            root = newStr.get(i)
            groups[root].append(i)
        
        for root in groups:
            orginal = groups[root].copy()
            orginal.sort()
            group = groups[root]
            group.sort(key = lambda x: s[x])
            
            for i in range(len(orginal)):
                ans[orginal[i]] = s[group[i]]

        return "".join(ans)
class disjointSets:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def get(self, a):
        if self.roots[a] == a:
            return a

        root = self.get(self.roots[a])
        self.roots[a] = root
        return root

    def union(self, a, b):
        rootA = self.get(a)
        rootB = self.get(b)
        

        if rootA == rootB:
            return

        if self.rank[rootA] == self.rank[rootB]:
            self.rank[rootA] += 1

        if self.rank[rootA] > self.rank[rootB]:
            self.roots[rootB] = rootA
            
        else:
            self.roots[rootA] = rootB