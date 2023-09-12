nums = [3,4,5,6,1,2]

left = 0
right = len(nums) - 1

result = nums[0]

while left <= right:
    if nums[right] >= nums[left]:
        result = min(result, nums[left])
        break
    
    mid = left + ((right - left)//2)
    result = min(result, nums[mid])
    if nums[mid] > nums[left]:
        left = mid + 1
    else:
        right = mid - 1

print(result)