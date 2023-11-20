#-------------Problem: 1239-----------

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(charset, string):
            c = Counter(charSet) + Counter(string)
            return max(c.values()) > 1

        def backtrack(index):
            if index == len(arr):
                return len(charSet)
            res = 0
            if not overlap(charSet, arr[index]):
                for c in arr[index]:
                    charSet.add(c)
                
                res = backtrack(index + 1)

                for c in arr[index]:
                    charSet.remove(c)
            
            return max(res,backtrack(index + 1))

        return backtrack(0)