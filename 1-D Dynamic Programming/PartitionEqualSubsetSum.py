#-------------Problem: 416--------------

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        DP = set()
        DP.add(0)
        target = sum(nums)//2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in DP:
                if t + nums[i] == target:
                    return True
                nextDP.add(t+nums[i])
                nextDP.add(t)
            DP = nextDP
        
        return False