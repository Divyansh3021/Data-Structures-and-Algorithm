nums = [-1,0,1,2,-1,-4]
target = 0

nums = sorted(nums)
index_arr = []

print("New array is: ",nums,"\n\n")
i = 0
k = len(nums) - 1

for i in range(len(nums)-2):
    j = i+1
    print("i: ",i)
    while  j < k:
        current_sum = nums[i] + nums[j] + nums[k]
        # print("Current numbers are:",nums[i]," ",nums[j]," ",nums[k])
        # print("Current sum: ",current_sum,"\n\n")
        if current_sum  == target:
            if ([nums[i],nums[j],nums[k]]) not in index_arr:
                index_arr.append([nums[i],nums[j],nums[k]])
            j += 1
        elif current_sum < target:
            j += 1
        else:
            k -= 1
    k = len(nums) - 1

print(index_arr)