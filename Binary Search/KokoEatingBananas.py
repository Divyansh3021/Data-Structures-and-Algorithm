piles = [3,6,7,11]
h = 8
import math

piles = sorted(piles)
left = 1
right = piles[-1]
result = piles[-1]

while left <= right:
    mid = left + ((right - left)//2)

    hours = 0
    for i in piles:
        hours += math.ceil(i/mid)
    print(f"Hours: {hours}")
    if hours <= h:
        result = min(result,mid)
        right = mid - 1
    else:
        left = mid + 1

print(result)