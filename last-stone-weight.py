class Solution:
    def lastStoneWeight(self, stones):
        if len(stones) < 2:
            return stones[0]
        stones = [-i for i in stones] #convert to max heap
        heapq.heapify(stones)
        while stones:
            
            if len(stones) >= 2:
                first = heapq.heappop(stones)
                second = heapq.heappop(stones)
                if first != second:
                    heapq.heappush(stones, first-second)  
            else:
                break
        if not stones:
            return 0 
        return -stones[0]