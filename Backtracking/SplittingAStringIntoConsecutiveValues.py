#-----------Problem: 1849----------

class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(index, prev):
            if index == len(s):
                return True
            for i in range(index, len(s)):
                val = int(s[index:i+1])

                if prev - val == 1 and backtrack(i+1, val):
                    return True
            return False
        
        for j in range(len(s) - 1):
            val = int(s[:j+1])
            if backtrack(j + 1, val):
                return True

        return False