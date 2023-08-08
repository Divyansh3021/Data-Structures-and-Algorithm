strs = ["flower","flow","flight"]

prefix = strs[0]

for i in range(len(strs) - 1):
    min_length = min(len(prefix), len(strs[i+1]))
    print(min_length)
    temp_prefix = ""
    for j in range(min_length):
        if prefix[j] == strs[i+1][j]:
            temp_prefix += strs[i][j]
    
    prefix = temp_prefix
    temp_prefix = ""

print(prefix)