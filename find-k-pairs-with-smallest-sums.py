class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        sums = []

        for i in range(n):
            curSum = nums1[i]
            for j in range(m):
                curSum += nums2[j]
                heapq.heappush(sums, (-curSum, nums1[i], nums2[j]))
        
                if len(sums) > k:
                    (summ,a,b) = heapq.heappop(sums)
                    if summ == -curSum:
                        break
                        
                curSum = nums1[i]

        return [i[1:] for i in sums]