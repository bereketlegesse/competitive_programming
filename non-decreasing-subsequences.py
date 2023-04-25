class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        container = []
        n = len(nums)
        cur = []

        def backtrack(index):
            if index == n:
                if len(cur)> 1 and cur not in container:
                    container.append(cur.copy())
                return
                 
            if not cur or cur[-1] <= nums[index] :
                cur.append(nums[index])
                backtrack(index + 1)
                cur.pop()

            backtrack(index + 1)
            
        backtrack(0)
        return container