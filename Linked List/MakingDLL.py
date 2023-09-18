class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def constructDLL(arr: [int]) -> Node:
    head = Node(arr[0])
    temp = head
    head.prev = None
    head.next = None

    for i in range(1, len(arr)):
        node_obj = Node(arr[i])
        head.next = node_obj
        node_obj.prev = head
        node_obj.next = None
        head = head.next
    
    return temp