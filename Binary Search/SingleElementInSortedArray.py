nums = [1,1,2,3,3,4,4,8,8]

left = 0
right = len(nums) -1 

while left <= right:
    mid = left + (right-left)//2

    if ((mid - 1 < 0)  or (nums[mid-1] != nums[mid])) and ((mid + 1 ==len(nums)) or (nums[mid] != nums[mid+1])):
        print(nums[mid])
    
    left_size = mid - 1 if nums[mid-1] == nums[mid] else mid

    if left_size % 2:
        right = mid - 1

    else:
        left = mid + 1