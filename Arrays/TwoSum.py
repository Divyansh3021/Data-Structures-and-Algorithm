nums = [-1, -2, -3, -4,-5]
target = -8

nums_copy = []
indices = []

for number in nums:
    nums_copy.append(number)

for number in nums_copy:
    number_index = nums.index(number)
    other_num = target - number
    if (other_num in nums) and (nums.index(other_num) != number_index):
        indices.append(number_index)
        indices.append(nums.index(other_num))
    

print(indices)