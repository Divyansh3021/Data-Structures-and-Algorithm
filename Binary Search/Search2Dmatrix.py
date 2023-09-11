matrix = [[1]]
target = 2

end_int = []
for i in range(len(matrix)):
    end_int.append(matrix[i][len(matrix[i])-1])

left = 0
right = len(end_int) - 1

if end_int[-1] < target:
    print(False)

while left <= right:
    mid = left + ((right-left)//2)

    if end_int[mid] > target:
        right = mid - 1
    
    elif end_int[mid] < target:
        left = mid + 1
    
    else:
        print(True)
        break

sub_array = left
print(f"Left: {left} Right: {right}")

left = 0
right = len(matrix[sub_array]) -1

while left <= right:
    mid = left + ((right-left)//2)

    if matrix[sub_array][mid] > target:
        right = mid - 1

    elif matrix[sub_array][mid] < target:
        left = mid + 1

    else:
        print(True)

else:
    print(False)