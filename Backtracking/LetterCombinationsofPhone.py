#------Problem: 17------
#-----T.C. = O(n*4^n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return res

        DigCharMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index, curStr):

            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for char in DigCharMap[digits[index]]:
                backtrack(index + 1, curStr + char)
        backtrack(0, "")
        return res