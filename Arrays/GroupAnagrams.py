strs = ["eat","tea","tan","ate","nat","bat"]

ana_array = []
for i in strs:
    i = (sorted(i))
    print(i)

for i in strs:
    temp_array = []
    for j in  strs:
        if i == j :
            temp_array.append(i)
    ana_array.append(temp_array)