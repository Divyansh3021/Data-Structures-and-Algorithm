class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    curr = head
    curr_data = curr.data
    curr = curr.next
    previous = curr.prev

    while curr.next:
        if curr.data == curr_data:
            previous.next = curr.next
            curr.next.prev = previous
        curr_data = curr.data
        curr = curr.next
        previous = curr.prev
    
    if curr.data == curr_data:
        previous.next = None
    return head
    pass
