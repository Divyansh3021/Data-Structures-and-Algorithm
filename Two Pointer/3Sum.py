nums = [-1,0,1,2,-1,-4]
target = 0

res = []
last_elem = nums[-1]

for k in range(len(nums)):
    first_complement = target - nums[k]
    print("First Complement is: ",first_complement)
    temp_arr = []

    for i in range(k+1,len(nums)):
        complement = first_complement - nums[i]
        print("Complement is: ",complement)
        if complement > last_elem:
            pass
        else:
            for j in range(i+1, len(nums)):
                if nums[j] == complement:
                    print("Complement found")
                    temp_arr.append(nums[k])
                    index_arr.append(i+1)
                    index_arr.append(j+1)
                    res.append(temp_arr)

print(res)