#-------------Problem: 494---------------

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #(index, total) -> no. of ways

        def helper(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in dp:
                return dp[(index, total)]
            dp[(index, total)] = ((helper(index + 1, total + nums[index])) + helper(index + 1, total - nums[index]))

            return dp[(index, total)]
        
        return helper(0,0)