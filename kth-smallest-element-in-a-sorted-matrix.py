class Solution(object):
    def kthSmallest(self, matrix, k):
        res = []
        for i in range(min(len(matrix),k)):
            res+=matrix[i]
        heapq.heapify(res)
        for i in range(k-1):
            heapq.heappop(res)
        return heapq.heappop(res)