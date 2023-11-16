#----------Problem: 90--------

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()
        def dfs(index):
            if index >= len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[index])
            dfs(index+1)

            cur.pop()

            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            dfs(index+1)

        dfs(0)
        return res