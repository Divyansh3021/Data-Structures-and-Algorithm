nums = [1,2]
k = 2

out_array = []
sorted_array = sorted(nums)

hashmap = {}

for i in sorted_array:
    if i not in hashmap.keys():
        hashmap[i] = 1
    
    else:
        hashmap[i] += 1

print(hashmap)

sorted_counts = sorted(hashmap.values())
sorted_counts.reverse()
# print(sorted_counts)

for i in range(k):
    max_count = sorted_counts[i]
    # print("for i = ", i," max count is: ", max_count, end=" ")
    for key in hashmap.keys():
        if hashmap[key] == max_count:
            hashmap[key] = -1
            out_array.append(key)

print(out_array)