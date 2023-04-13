class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxLen = 0
        N = len(arr)
        subseq = Counter()

        def backtrack(index):
            nonlocal subseq
            nonlocal maxLen
            if index >= N:
                length = sum(list(subseq.values()))
                maxLen = max(maxLen, length)
                return
            curWord = arr[index]
            for i in curWord:
                if i in subseq:
                    backtrack(index + 1)
                    break
            else:
                if max(Counter(curWord).values()) <= 1:
                    subseq += Counter(curWord)
                    backtrack(index+1)
                    subseq -= Counter(curWord)
                backtrack(index+1)

        backtrack(0)
        return maxLen