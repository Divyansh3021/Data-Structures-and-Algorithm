nums = [3,9,6]
k = 2

nums.sort()
res, total = 0,0

l, r = 0,0

while r < len(nums):
    total += nums[r]

    while nums[r]*(r-l+1) >= total + k:
        total -= nums[l]
        l += 1 
    
    res = max(res, r-l+1)
    r += 1

print(res)