matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

end_int = []
for i in len(matrix):
    end_int.append(matrix[i][len(m[i]-1)])

left = 0
right = len(end_int) - 1

while left <= right:
    mid = left + ((right-left)//2)

    if end_int[mid] > target:
        right = mid - 1
    
    elif end_int[mid] < target:
        left = mid + 1
    
    else:
        print(True)
