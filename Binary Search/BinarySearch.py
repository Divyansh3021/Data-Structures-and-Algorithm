nums = [-1,0,3,5,9,12]
target = 9

def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right)//2

        if nums[mid] > target:
            right -= 1
        
        elif nums[mid] < target:
            left += 1
        
        else:
            return mid

print(search(nums, target))