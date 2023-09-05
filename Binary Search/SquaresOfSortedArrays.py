nums = [-4,-1,0,3,10]


res = []
left = 0
right = len(nums) - 1

while left <= right:
    if nums[left]**2 > nums[right]**2:
        res.append(nums[left]**2)
        left += 1
    
    else:
        res.append(nums[right]**2)
        right -= 1

print(res[::-1])