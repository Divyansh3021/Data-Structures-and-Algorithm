from heapq import *

min_heap = []

for i in range(13, 0, -1):
    print("i: ",i, end=" ")
    heappush(min_heap, i)
    print("Heap: ",min_heap)

while min_heap:
    print(heappop(min_heap))