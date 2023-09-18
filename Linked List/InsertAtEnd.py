class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


# Please do not change code above.


def insertAtTail(head: Node, k: int) -> Node:
    if head:
        curr = head

        while curr.next != None:
            curr = curr.next
        
        node_obj = Node(k)

        curr.next = node_obj
        node_obj.prev = curr
        node_obj.next = None
        return head
        pass
    else:
        node_obj = Node(k)
        node_obj.next = None
        node_obj.prev = None
        return node_obj