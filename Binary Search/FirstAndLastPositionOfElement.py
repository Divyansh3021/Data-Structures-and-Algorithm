nums = [5, 7,7,8,8,10]
target = 8

def binarySearch(nums, target, bias):
    left, right = 0, len(nums)-1
    i = -1

    while left <= right :

        mid = left + (right - left)//2

        if nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1
        
        else:
            i = mid
            if bias:
                left = mid + 1
            else:
                right = mid - 1
    
    return i

left = binarySearch(nums, target, False)
right = binarySearch(nums, target, True)

print([left, right])