#-----------------Problem: 1647-----------------

class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        res = 0
        freq = set()

        for c, val in count.items():
            while val > 0 and val in freq:
                val -= 1
                res += 1
            freq.add(val)
        return res