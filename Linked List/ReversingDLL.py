'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

def reverseDLL(head):
    temp = None
    curr = head

    while curr != None:
        # print("Current element:", curr.data)
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp

        curr = curr.prev
    
    if temp is not None:
        return temp.prev
    else:
        return head
    pass