#-----------------Problem: 1578-----------------

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        for i in range(len(colors) - 1):
            curr = colors[i]
            next_color = colors[i + 1]
            if curr == next_color:
                ans += min(neededTime[i], neededTime[i + 1])
                neededTime[i + 1] = max(neededTime[i], neededTime[i + 1])
        return ans