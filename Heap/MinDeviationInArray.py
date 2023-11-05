#------- Problem: 1675---------

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        result = float("inf")
        heap = []
        for i in nums:
            if i%2 == 0:
                heapq.heappush(heap, -1*i)
            else:
                heapq.heappush(heap, -2*i)
        heap_min = -1 * max(heap)
        while heap[0] % 2 == 0:
            heap_max = -1 * heappop(heap)
            heappush(heap, -1 * heap_max//2)
            result = min(result, heap_max - heap_min)
            heap_min = min(heap_min, heap_max//2)
        heap_max = (-1) * heappop(heap)
        result = min(result, heap_max - heap_min)
        return result