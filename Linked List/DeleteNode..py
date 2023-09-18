class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Please do not change code above.


def deleteLast(list: Node) -> Node:
    head=list
    if head is None:
        return None
    if head.next is None:
        del head
        return None
    current=head
    while current.next.next:
        current=current.next
    del current.next
    current.next=None
    return head            
    pass