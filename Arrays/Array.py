nums = [3,2,4]
target = 6
nums_copy = []
indices = []

for number in nums:
    nums_copy.append(number)

for number in nums_copy:
    if number > target:
        pass
    else:
        indices.append(nums.index(number))
        print("\n\n\nnums before removal: ",nums, " number is: ", number)
        nums.remove(number)
        other_num = target - number
        print("after removal: ",nums)
        if other_num in nums:
            # print(nums.index(other_num))
            indices.append(nums.index(other_num) + 1)
            break
        else:
            indices = []
            nums = nums_copy
            print("after everything: ", nums)
            pass
print(indices)