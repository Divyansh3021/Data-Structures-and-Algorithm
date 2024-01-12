#----------------problem: 1911-----------------

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}

        def helper(i, even = True):
            if i == len(nums):
                return 0
            
            if (i, even) in dp:
                return dp[(i, even)]
            
            num = nums[i] if even else (-1 * nums[i])
            dp[(i, even)] = max(num + helper(i+1, not even), helper(i+1, even))
            return dp[(i, even)]
        return helper(0)