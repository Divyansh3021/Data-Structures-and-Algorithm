#------Problme: 78------
#------T.C. = O(n*2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                powerSet.append(subset.copy())
                return

            #If nums[index] is chosen
            subset.append(nums[index])
            dfs(index + 1)

            #If nums[index] is not chosen
            subset.pop()
            dfs(index + 1)
        dfs(0)
        return powerSet