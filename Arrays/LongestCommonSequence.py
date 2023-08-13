nums = [0,3,7,2,5,8,4,6,0,1]

sorted_list = sorted(nums)
length_arr =[]
length = 1

if len(sorted_list == 0):
    print(0)

elif len(sorted_list) == 1:
    print(1)
for i in range(len(sorted_list)-1):
    # print(sorted_list[i])
    if sorted_list[i+1] == sorted_list[i] + 1:
        length += 1

    elif sorted_list[i+1] == sorted_list[i]:
        length = length

    else:
        print("Length arr is: ", length_arr)
        length = 1
    length_arr.append(length)
    # print("Length is: ",length)

print(max(length_arr))