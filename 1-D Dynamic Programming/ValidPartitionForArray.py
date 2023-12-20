#---------------Problem:2369--------------

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = {}
        def helper(i):
            if i == len(nums):
                return True
            if i in dp:
                return dp[i]
            res = False
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                res = helper(i + 2)

            if i < len(nums) - 2:
                if (nums[i] + 1 == nums[i+1] == nums[i + 2] - 1) or (nums[i] == nums[i+1] == nums[i+2]):
                    res = res or helper(i + 3)

            dp[i] = res
            return res
        
        return helper(0)