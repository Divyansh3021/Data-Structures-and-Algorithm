arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

window = []
count = 0
sum = sum(arr[:k-1])
left = 0

for i in range(k-1,len(arr)):
    sum += arr[i]
    if sum//k >= threshold:
        count += 1
    sum -= arr[left]
    left += 1
    
print(count)