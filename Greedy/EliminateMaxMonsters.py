#------------Problem: 1921-------------

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minReach = dist
        for i in range(len(dist)):
            minReach[i] = dist[i] / speed[i]
        minReach = sorted(minReach)
        count = 0
        for i in minReach:
            if i <= count:
                break
            count += 1
        return count