#------------Problem: 1980-----------


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = {s for s in nums }

        def backtrack(index, num):
            if index == len(nums):
                res = "".join(num)
                return None if res in nums else res

            res = backtrack(index + 1, num)
            if res: return res

            num[index] = "1"
            res = backtrack(index + 1, num)
            if res: return res

        return backtrack(0, ["0" for i in nums])