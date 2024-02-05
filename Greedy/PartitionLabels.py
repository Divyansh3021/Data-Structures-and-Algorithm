#-------------Problem: 763-------------

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}
        for i in range(len(s)):
            map[s[i]] = i

        res = []
        cur_len = 0
        end = 0

        for i in range(len(s)):
            end = max(end, map[s[i]])
            cur_len += 1   
            if i == end:
                res.append(cur_len)
                cur_len = 0
        return res