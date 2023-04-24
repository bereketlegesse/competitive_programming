class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        p1 = 0
        p2 = 0
        merge = []

        while p1 < n and p2 < m:
            if word1[p1] > word2[p2]:
                merge.append(word1[p1])
                p1 += 1
            elif word2[p2] > word1[p1]:
                merge.append(word2[p2])
                p2 += 1
            else:
                if word1[p1:] > word2[p2:]:
                    merge.append(word1[p1])
                    p1 += 1
                else:
                    merge.append(word2[p2])
                    p2 += 1
                    
        if p1 < n:
            merge.append(word1[p1:])
        elif p2 < m:
            merge.append(word2[p2:])

        return "".join(merge)