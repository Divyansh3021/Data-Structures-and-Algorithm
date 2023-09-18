class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.


def constructLL(arr: [int]) -> Node:
    head = Node(arr[0])
    head.next = None
    temp = head
    for i in range(1,len(arr)):
        
        Node_obj = Node(arr[i])

        if i != len(arr):
            temp.next = Node_obj
        else:
            temp.next = None
        temp = temp.next    
    
    return head