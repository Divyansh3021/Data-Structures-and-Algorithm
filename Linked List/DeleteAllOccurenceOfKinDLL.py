class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:
    curr = head
    previous = curr.prev

    while curr.next:
        # print("Current Node: ",curr.data)
        if curr.data == k:
            if previous:
                previous.next = curr.next
                curr.next.prev = previous
            else:
                head = curr.next
                curr.next.prev = None
        curr = curr.next
        previous = curr.prev
    
    if curr.data == k:
        if previous:
            previous.next = None
        else:
            head = None
    return head
    pass

