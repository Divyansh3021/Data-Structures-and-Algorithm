def findMiddle(head):
    #traversing the linked list
    count = 0
    curr = head

    while curr:
        curr = curr.next
        count+=1
    # print("Count is: ",count)
    
    #middle element
    mid_elem = count//2 + 1
    temp = head
    for i in range(1, mid_elem):
        temp = temp.next

    return temp
    pass