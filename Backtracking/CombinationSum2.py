#-----Problem: 40-----

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, cur, curSum):
            if curSum == target:
                res.append(cur[:])
                return 

            if index >= len(candidates) or curSum > target:
                return

            cur.append(candidates[index])
            backtrack(index + 1, cur, curSum+candidates[index])

            cur.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, cur, curSum)

        backtrack(0, [], 0)
        return res