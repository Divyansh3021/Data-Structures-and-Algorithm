#-----------Problem: 93-----------
#T.C. 3^5

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if len(s) > 12:
            return res

        def backtrack(index, dots, curIP):
            if dots == 4 and index == len(s):
                res.append(curIP[:-1])
                return 
            
            if dots > 4:
                return

            for j in range(index, min( index + 3, len(s))):
                if int(s[index:j+1]) < 256 and (index==j or s[index]!="0"):
                    backtrack(j+1, dots + 1, curIP + s[index:j+1] + ".")
        backtrack(0, 0, "")
        return res