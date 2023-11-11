#-----Problem: 1985------


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for i in range(len(nums)):
            heappush(heap, int(nums[i]))
            if len(heap) > k:
                heappop(heap)
        

        return str(heap[0])