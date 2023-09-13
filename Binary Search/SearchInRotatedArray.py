nums = [4, 1,3]
target = 3

left, right = 0, len(nums) - 1

while left <= right:
    mid = left + ((right - left)//2)
    print("Current Mid element: ",nums[mid])

    if nums[mid] == target:
        print(mid)
        break
    
    if nums[mid] >= nums[left]: #left portion of the array
        if target > nums[mid] or target < nums[left]:
            left = mid + 1

        else:
            right = mid - 1
    
    else: #right portion
        if target < nums[mid] or target > nums[right]:
            right = mid - 1
        else: left = mid + 1

else:
    print(-1)