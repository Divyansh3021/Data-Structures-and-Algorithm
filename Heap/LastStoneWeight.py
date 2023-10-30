class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heappush(heap, -1 * i)

        while len(heap) > 1:
            stone1 = heappop(heap)
            stone2 = heappop(heap)
            if abs(stone2 - stone1): heappush(heap,-1 * abs(stone2 - stone1))
        
        if heap: 
            return -1 * heap[0]
        else: 
            return 0
