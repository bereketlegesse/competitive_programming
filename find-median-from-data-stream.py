class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and self.minheap[0] <= num:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        if len(self.maxheap) - 1 > len(self.minheap):
            heapq.heappush(self.minheap, -1*heapq.heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap,-1* heapq.heappop(self.minheap))
        
    def findMedian(self) -> float:
        if len(self.minheap) < len(self.maxheap):
            return -self.maxheap[0]

        return (self.minheap[0] - self.maxheap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()