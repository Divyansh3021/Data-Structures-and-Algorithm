#-------Problem: 39------
#-------T.C. O(2^target)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            
            if index >= len(candidates) or total > target:
                return
            
            #If we can choose the current element
            cur.append(candidates[index])
            dfs(index, cur, total+candidates[index])

            #If we can't choose the current element
            cur.pop()
            dfs(index + 1, cur, total)

        dfs(0, [], 0)
        return result