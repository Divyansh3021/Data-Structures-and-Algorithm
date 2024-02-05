#-------------------Problem: 1899----------------------

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0,0,0]
        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue
            res = [max(res[0], i[0]), max(res[1], i[1]), max(res[2], i[2])]
        
        return True if res == target else False