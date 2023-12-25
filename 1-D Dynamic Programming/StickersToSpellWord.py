#----------------------Problem: 691------------------------

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickCount = []
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = 1 + stickCount[i].get(c,0)

        dp = {} #key = subseq of target, val = min no. of stickers
        def helper(target, sticker):
            if target in dp:
                return dp[target]
            
            res = 1 if sticker else 0
            remainT = ""
            for c in target:
                if c in sticker and sticker[c] > 0:
                    sticker[c] -= 1
                else:
                    remainT += c
            
            if remainT:
                used = float("inf")
                for s in stickCount:
                    if remainT[0] not in s:
                        continue
                    used = min(used, helper(remainT, s.copy()))
                dp[remainT] = used
                res += used
            return res
        
        res = helper(target, {})
        return res if res != float("inf") else -1