class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Do not change code above.


def deleteLastNode(head: Node) -> Node:
    if head.next:
        prev = None
        curr = head

        while curr.next :
            prev = curr
            curr = curr.next
        
        prev.next = None
        curr.prev = None
        del curr
        return head
        pass
    else:
        return None