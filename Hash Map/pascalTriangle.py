numRows = 3
hashMap = {}

for i in range(numRows):
    print(i)
    if i == 0:
        hashMap[i] = [1]
    
    else:
        prevArr = hashMap[i-1]  #prevArr = [1]
        currArr = [[None] for k in range(i+1)]
        for j in range(i+1):
            print("j: ",j)
            if j == 0  or j == i:
                currArr[j] = 1
            elif len(prevArr) >= j+1:
                currArr[j] = prevArr[j-1] + prevArr[j]
        hashMap[i] = currArr
    print(hashMap.values())
    