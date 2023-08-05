class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        temp = self.head

        while temp!=None:
            print(temp.data)
            temp = temp.next

    def reverse_traverse(self, tail):
        temp = tail

        while (temp != self.head):
            print("Current Node: ", temp.data)
            print("Prev node: ", temp.prev.data)
            # print(temp.data)
            temp = temp.prev
    
head = DoublyLinkedList()
first = Node(10)
second = Node(20)
third = Node(30)

head.head = first
first.prev = head
first.next = second
second.prev = first
second.next = third
third.prev = second

print("Linked list in forward order is : ")
head.traverse()

print("\n\nLinked List in reverse order is: ")
head.reverse_traverse(third)