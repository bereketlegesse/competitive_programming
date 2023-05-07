class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heapp = []
        heapq.heappush(heapp,(1, nums[0]))
        n = len(nums)

        i = 1
        while i < n:
            num = nums[i]
            waiting = []
            curLen = len(heapp)

            while heapp:  
                a,lastNum = heapq.heappop(heapp)
                if num == lastNum + 1:
                    heapq.heappush(heapp, (a+1, num))
                    break
                waiting.append((a, lastNum))

            if len(waiting) == curLen:
                heapq.heappush(heapp,(1,num))
            
            for pair in waiting:
                if pair[0] < 3 and pair[1]+1 < num :
                    return False
                heapq.heappush(heapp, pair)
            
            i += 1
        pair = heapq.heappop(heapp)

        return pair[0] > 2