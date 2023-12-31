#------------------Problem: 1624--------------------


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        index = {}
        res = -1
        for i, char in enumerate(s):
            if char in index:
                diff = i - index[char]
                res = max(res, diff)
            else:
                index[char] = i
        
        return res -1 if res!= -1 else -1