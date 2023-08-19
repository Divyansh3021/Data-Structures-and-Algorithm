heights = [1,2,3,4,5,25,24,3,4]

i = 0
j = len(heights) - 1

capactiy = 0

while i < j:
    print("i: {}, j: {}".format(i,j))
    width = j - i
    height_i, height_j = heights[i], heights[j]
    height = min(height_i,height_j)

    print("Height: {} width: {} ".format(height,width))
    next_max_min_height_1 = min(heights[i], heights[j-1])
    next_max_min_height_2 = min(heights[i+1], heights[j])

    print("next_max_min_height_1 : {}, next_max_min_height_2: {}".format(next_max_min_height_1,next_max_min_height_2))
    if capactiy < height*width:
        capactiy = height*width
        print("New Capacity is: ",capactiy)
        i += 1

    elif next_max_min_height_1 < next_max_min_height_2:
        i += 1
    
    else:
        j -= 1
    
print(capactiy)