#----Problem: 1094----

#T.C. = O(nlogn)

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        currPass = 0
        minHeap = []  #minHeap[i] = [end, numpass]

        for t in trips:
            numPass, start, end = t

            while minHeap and minHeap[0][0] <= start:
                currPass -= minHeap[0][1]
                heappop(minHeap)
            
            heappush(minHeap, [end, numPass])
            currPass += numPass

            if currPass > capacity:
                return False
        return True
