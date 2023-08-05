class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head

        while (temp!= None):
            print(temp.data)
            temp = temp.next

    def insertAfter(self, number, data):
        temp = self.head

        while (temp.data != number):
            temp = temp.next
        
        after_temp = temp.next
        insNode = Node(data)
        temp.next = insNode
        insNode.next = after_temp
    
    def deleteNode(self, number):
        temp = self.head

        while(temp.data != number):
            prev = temp
            temp = temp.next

        prev.next = temp.next
        

myLL = LinkedList()
first = Node(10)
second = Node(20)
third = Node(30)

myLL.head = first
first.next = second
second.next = third

print("Before Deletion: ")
myLL.printList()

myLL.deleteNode(20)
print("After Deletion: ")
myLL.printList()