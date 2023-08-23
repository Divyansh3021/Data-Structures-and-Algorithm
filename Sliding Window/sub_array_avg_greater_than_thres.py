arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

count = 0
window = arr[:k]
sum = 0
for i in window: sum+=i
avg = sum/k

if avg > threshold:
    count+=1

for i in range(len(arr)-k+1):
    if len(window) > k:
        window.pop(0)
    if avg > threshold:
        count+=1