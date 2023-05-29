class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()
        n = len(nums)
        
        def backtrack(index, summ):
            if index == n:
                return summ == target

            if (index, summ) in memo:
                return memo[(index, summ)]

            ans = backtrack(index + 1, summ + nums[index])
            ans += (backtrack(index + 1, summ - nums[index]))
            memo[(index, summ)] = ans
            return ans

        return backtrack(0, 0)