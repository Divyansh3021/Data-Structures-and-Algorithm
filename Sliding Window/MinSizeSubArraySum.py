target = 7
nums = [2,3,1,2,4,3]

left = 0 
total = 0
min_size = len(nums)
size = 0

for right in range(len(nums)):
    total += nums[right]

    while total >= target:
        total -= nums[left]
        min_size = min(min_size, right-left+1)
        left += 1
    

print(min_size)