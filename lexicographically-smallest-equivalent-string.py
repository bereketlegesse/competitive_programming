class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        newStr = disjointSets()
        answer = []
        for i in range(n):
            newStr.union(s1[i], s2[i])
            
            
        for i in range(len(baseStr)):
            answer.append(newStr.minn[ord(newStr.get(baseStr[i]))-97])        
        return  "".join(answer)

class disjointSets:
    def __init__(self):
        self.roots = [chr(i) for i in range(97,123)]
        self.minn = [chr(i) for i in range(97,123)]

    def get(self, a):
        idx = ord(a) - 97
        if self.roots[idx] == a:
            return a

        root = self.get(self.roots[idx])
        self.roots[idx] = root
        return root

    def union(self, a, b):
        rootA = self.get(a)
        rootB = self.get(b)
        if rootA == rootB:
            return
            
        idxA = ord(rootA)-97
        idxB = ord(rootB)-97
        self.roots[idxA] = rootB
        self.minn[idxB] = min(self.minn[idxA],self.minn[idxB])