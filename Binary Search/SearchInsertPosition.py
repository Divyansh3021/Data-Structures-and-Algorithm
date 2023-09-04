nums = [1,3,5,6]
target = 2

left = 0
right = len(nums) - 1

while left <= right:
    print("Left: ", left, " Right: ", right)
    mid = (left+right)//2

    if nums[mid] < target:
        left = mid + 1

    elif nums[mid] > target:
        right = mid - 1
    
    else:
        print(mid)
        break


print(left)
