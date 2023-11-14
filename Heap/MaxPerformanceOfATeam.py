#-----Problem: 1383-----
#-----T.C. = nlogn due to sorting and nlogK due to heap 
#-----Overall T.C. = nlogn

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = []
        for eff, speed in zip(efficiency, speed):
            engineers.append([eff, speed])
        engineers.sort(reverse = True)

        heap = []
        res, totalSpeed = 0, 0

        for eff, speed in engineers:
            if len(heap) == k:
                totalSpeed -= heappop(heap)
            
            totalSpeed += speed
            heappush(heap, speed)
            res = max(res, eff * totalSpeed)
        return res % (10**9 + 7)