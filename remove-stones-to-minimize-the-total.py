class Solution(object):
    def minStoneSum(self, piles, k):
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for i in range(k):
            pile = -1*heapq.heappop(piles)    
            pile -= (pile//2)
            heapq.heappush(piles,-1*pile)

        piles = [-pile for pile in piles]
        return sum(piles)