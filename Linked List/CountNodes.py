'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    count = 1
    while head.next != None:
        # print("Current count:",count)
        head = head.next
        count += 1
    return count
