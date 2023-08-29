arr = [1,2,3,4,5]
k = 4
x = 3

left = 0
diff = {}
for i in range(len(arr)):
    diff[arr[i]] = abs(x - arr[i])

sorted_values = sorted(diff.values())
values = []
for value in range(k):
    values.append(value)

i = 0
keys = []
for key in diff.keys():
    if diff[key] == values[i]:
        keys.append(key)
        i += 1
print(keys)