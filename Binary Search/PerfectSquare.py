num = 2000105819

# arr = []
# for i in range(num+1):
#     arr.append(i)

left = 0
right = num
# print(arr)

while left <= right:    
    mid = (left+right)//2

    if mid**2 < num:
        left = mid + 1
    
    elif mid**2 > num:
        right = mid - 1
    
    else:
        print(True)
        break
else:
    print(False)